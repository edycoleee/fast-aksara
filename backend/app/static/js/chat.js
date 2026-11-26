(() => {
  "use strict";

  const currentUserId = Number(window.chatCurrentUserId);
  const elements = {
    attachmentButton: document.getElementById("attachmentButton"),
    attachmentInput: document.getElementById("attachmentInput"),
    attachmentName: document.getElementById("attachmentName"),
    chatError: document.getElementById("chatError"),
    clearButton: document.getElementById("clearChatButton"),
    connection: document.getElementById("connectionStatus"),
    conversationList: document.getElementById("conversationList"),
    emptyState: document.getElementById("emptyState"),
    form: document.getElementById("messageForm"),
    input: document.getElementById("messageInput"),
    menuButton: document.getElementById("menuButton"),
    messages: document.getElementById("messages"),
    partnerAvatar: document.getElementById("partnerAvatar"),
    partnerName: document.getElementById("partnerName"),
    partnerStatus: document.getElementById("partnerStatus"),
    sendButton: document.getElementById("sendButton"),
    sidebar: document.getElementById("chatSidebar"),
    newChatButton: document.getElementById("newChatButton"),
  };

  let activeConversation = null;
  let lastMessageId = 0;
  let messageVersion = 0;
  let polling = false;
  let lastHeartbeat = 0;
  let lastConversationRefresh = 0;
  let pollingTimer = null;

  async function api(url, options = {}) {
    const response = await fetch(url, {
      credentials: "same-origin",
      ...options,
      headers: {
        ...(options.body instanceof FormData
          ? {}
          : { "Content-Type": "application/json" }),
        ...(options.headers || {}),
      },
    });
    if (response.status === 401) {
      window.location.assign("/chat/login");
      throw new Error("Sesi chat berakhir.");
    }
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const detail = data.detail || "Permintaan chat gagal.";
      throw new Error(detail);
    }
    return data;
  }

  function setError(message = "") {
    elements.chatError.textContent = message;
    elements.chatError.hidden = !message;
  }

  function setConnection(connected, message = "") {
    elements.connection.textContent = message || (connected ? "Terhubung" : "Koneksi terputus");
  }

  function timeText(value) {
    const date = new Date(value);
    const now = new Date();
    const day = (item) => new Date(item.getFullYear(), item.getMonth(), item.getDate()).getTime();
    const time = date.toLocaleTimeString("id-ID", {
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    });
    if (day(date) === day(now)) return time;
    const yesterday = new Date(now);
    yesterday.setDate(now.getDate() - 1);
    if (day(date) === day(yesterday)) return `Kemarin, ${time}`;
    const withYear = date.getFullYear() !== now.getFullYear();
    return `${date.toLocaleDateString("id-ID", {
      day: "numeric",
      month: "short",
      ...(withYear ? { year: "numeric" } : {}),
    })}, ${time}`;
  }

  function dateLabel(value) {
    const date = new Date(value);
    const now = new Date();
    const dateOnly = (item) => new Date(item.getFullYear(), item.getMonth(), item.getDate()).getTime();
    if (dateOnly(date) === dateOnly(now)) return "Hari ini";
    const yesterday = new Date(now);
    yesterday.setDate(now.getDate() - 1);
    if (dateOnly(date) === dateOnly(yesterday)) return "Kemarin";
    return date.toLocaleDateString("id-ID", {
      weekday: "long",
      day: "numeric",
      month: "long",
      year: "numeric",
    });
  }

  function clearMessages(emptyTitle = "Belum ada pesan") {
    elements.messages.replaceChildren();
    const state = elements.emptyState.cloneNode(true);
    state.querySelector("h2").textContent = emptyTitle;
    state.querySelector("p").textContent = activeConversation
      ? "Kirim pesan pertama untuk memulai percakapan."
      : "Pilih pengguna di daftar atau tekan tombol tambah.";
    elements.messages.append(state);
  }

  function messageDay(message) {
    return new Date(message.created_at).toLocaleDateString("id-ID");
  }

  function renderMessage(message, forceBottom = false) {
    const empty = elements.messages.querySelector(".chat-empty-state");
    if (empty) empty.remove();

    const previous = elements.messages.querySelector(".chat-bubble-row:last-of-type");
    const previousDay = previous ? previous.dataset.day : "";
    if (previousDay !== messageDay(message)) {
      const divider = document.createElement("div");
      divider.className = "chat-date-divider";
      divider.textContent = dateLabel(message.created_at);
      elements.messages.append(divider);
    }

    const row = document.createElement("div");
    row.className = `chat-bubble-row${message.sender_id === currentUserId ? " mine" : ""}`;
    row.dataset.day = messageDay(message);

    const bubble = document.createElement("article");
    bubble.className = "chat-bubble";

    if (message.attachment) {
      const attachment = document.createElement("a");
      attachment.className = "chat-attachment";
      attachment.href = message.attachment.url;
      attachment.target = "_blank";
      attachment.rel = "noopener";
      if (message.attachment.type === "image") {
        const image = document.createElement("img");
        image.src = message.attachment.preview_url;
        image.alt = message.attachment.name || "Foto kiriman";
        image.loading = "lazy";
        image.addEventListener("error", () => {
          image.remove();
          const fallback = document.createElement("div");
          fallback.className = "chat-file-card";
          fallback.textContent = `🖼 ${message.attachment.name || "Gambar"}`;
          attachment.append(fallback);
        }, { once: true });
        attachment.append(image);
      } else {
        const card = document.createElement("div");
        card.className = "chat-file-card";
        card.innerHTML = "<span aria-hidden=\"true\">📄</span>";
        const name = document.createElement("span");
        name.className = "chat-file-name";
        name.textContent = message.attachment.name || "Dokumen PDF";
        card.append(name);
        attachment.append(card);
      }
      bubble.append(attachment);
    }

    if (message.content) {
      const content = document.createElement("div");
      content.className = "chat-bubble-content";
      content.textContent = message.content;
      bubble.append(content);
    }

    const time = document.createElement("time");
    time.className = "chat-bubble-time";
    time.dateTime = message.created_at;
    time.title = new Date(message.created_at).toLocaleString("id-ID");
    time.textContent = timeText(message.created_at);
    bubble.append(time);
    row.append(bubble);
    elements.messages.append(row);

    if (forceBottom || elements.messages.scrollHeight - elements.messages.scrollTop - elements.messages.clientHeight < 180) {
      elements.messages.scrollTop = elements.messages.scrollHeight;
    }
  }

  function statusMarkup(online) {
    const dot = document.createElement("span");
    dot.className = online ? "chat-online-dot" : "chat-offline-dot";
    const text = document.createTextNode(online ? "Online" : "Offline");
    const fragment = document.createDocumentFragment();
    fragment.append(dot, text);
    return fragment;
  }

  function personButton(item, onClick) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "chat-person";
    if (activeConversation && activeConversation.id === item.id) {
      button.classList.add("active");
    }
    const avatar = document.createElement("span");
    avatar.className = "chat-avatar";
    avatar.textContent = (item.partner_name || item.display_name || "?").slice(0, 1).toUpperCase();
    const main = document.createElement("span");
    main.className = "chat-person-main";
    const name = document.createElement("strong");
    name.className = "chat-person-name";
    name.textContent = item.partner_name || item.display_name;
    const preview = document.createElement("span");
    preview.className = "chat-person-preview";
    preview.textContent = item.last_message || (item.is_online ? "Online" : "Offline");
    main.append(name, preview);
    const time = document.createElement("span");
    time.className = "chat-person-time";
    time.textContent = item.last_message_at ? timeText(item.last_message_at) : "";
    button.append(avatar, main, time);
    button.addEventListener("click", () => onClick(item));
    return button;
  }

  async function refreshConversations() {
    const conversations = await api("/chat/api/conversations");
    elements.conversationList.replaceChildren();
    if (!conversations.length) {
      elements.conversationList.append(Object.assign(document.createElement("p"), {
        className: "chat-muted",
        textContent: "Belum ada percakapan. Tekan tombol +.",
      }));
      return;
    }
    conversations.forEach((item) => {
      elements.conversationList.append(personButton(item, () => openConversation(item)));
    });
  }

  async function showUsers() {
    try {
      const users = await api("/chat/api/users");
      elements.conversationList.replaceChildren();
      if (!users.length) {
        elements.conversationList.append(Object.assign(document.createElement("p"), {
          className: "chat-muted",
          textContent: "Belum ada pengguna chat lain.",
        }));
        return;
      }
      users.forEach((user) => {
        const item = {
          id: 0,
          partner_id: user.id,
          partner_name: user.display_name,
          is_online: user.is_online,
        };
        elements.conversationList.append(personButton(item, async () => {
          try {
            const conversation = await api("/chat/api/conversations", {
              method: "POST",
              body: JSON.stringify({ partner_id: user.id }),
            });
            await openConversation(conversation);
            await refreshConversations();
          } catch (error) {
            setError(error.message);
          }
        }));
      });
    } catch (error) {
      setError(error.message);
    }
  }

  function setComposerEnabled(enabled) {
    elements.input.disabled = !enabled;
    elements.attachmentButton.disabled = !enabled;
    elements.clearButton.disabled = !enabled || !activeConversation;
    elements.sendButton.disabled = !enabled || !activeConversation;
  }

  async function openConversation(item) {
    activeConversation = item;
    lastMessageId = 0;
    messageVersion = item.message_version;
    elements.partnerName.textContent = item.partner_name;
    elements.partnerAvatar.textContent = item.partner_name.slice(0, 1).toUpperCase();
    elements.partnerStatus.replaceChildren(statusMarkup(item.is_online));
    elements.sidebar.classList.remove("open");
    clearMessages();
    setComposerEnabled(true);
    setError();
    const data = await loadMessages();
    if (!data.messages.length) elements.clearButton.disabled = true;
    elements.input.focus();
  }

  async function loadMessages() {
    if (!activeConversation) return { messages: [] };
    const data = await api(
      `/chat/api/conversations/${activeConversation.id}/messages?after_id=${lastMessageId}&limit=100`
    );
    if (data.message_version !== messageVersion) {
      messageVersion = data.message_version;
      clearMessages();
      lastMessageId = 0;
      const reset = await api(
        `/chat/api/conversations/${activeConversation.id}/messages?after_id=0&limit=100`
      );
      reset.messages.forEach((message) => renderMessage(message));
      lastMessageId = reset.last_message_id;
      elements.clearButton.disabled = reset.messages.length === 0;
      return reset;
    }
    data.messages.forEach((message) => renderMessage(message, true));
    lastMessageId = data.last_message_id;
    if (data.messages.length) elements.clearButton.disabled = false;
    return data;
  }

  async function poll() {
    if (polling || document.hidden) return;
    polling = true;
    try {
      const now = Date.now();
      if (activeConversation) await loadMessages();
      if (now - lastHeartbeat >= 20000) {
        await api("/chat/api/heartbeat", { method: "POST" });
        lastHeartbeat = now;
      }
      if (now - lastConversationRefresh >= 20000) {
        await refreshConversations();
        lastConversationRefresh = now;
      }
      setConnection(true);
      setError();
    } catch (error) {
      setConnection(false);
      setError(error.message);
    } finally {
      polling = false;
    }
  }

  function updateAttachmentName() {
    const file = elements.attachmentInput.files[0];
    elements.attachmentName.textContent = file ? `Lampiran: ${file.name}` : "";
    elements.attachmentName.hidden = !file;
  }

  async function sendMessage(event) {
    event.preventDefault();
    if (!activeConversation) return;
    const file = elements.attachmentInput.files[0];
    const content = elements.input.value.trim();
    if (!content && !file) return;

    setComposerEnabled(false);
    setError();
    try {
      let message;
      if (file) {
        const body = new FormData();
        body.append("file", file);
        body.append("content", content);
        message = await api(
          `/chat/api/conversations/${activeConversation.id}/attachments`,
          { method: "POST", body }
        );
      } else {
        message = await api(
          `/chat/api/conversations/${activeConversation.id}/messages`,
          { method: "POST", body: JSON.stringify({ content }) }
        );
      }
      renderMessage(message, true);
      lastMessageId = message.id;
      elements.input.value = "";
      elements.attachmentInput.value = "";
      updateAttachmentName();
      elements.clearButton.disabled = false;
      await refreshConversations();
    } catch (error) {
      setError(error.message);
    } finally {
      setComposerEnabled(true);
      elements.input.focus();
    }
  }

  async function clearChat() {
    if (!activeConversation) return;
    const confirmed = window.confirm(
      "Hapus semua pesan dalam percakapan ini untuk kedua pengguna?\nTindakan ini tidak dapat dibatalkan."
    );
    if (!confirmed) return;
    elements.clearButton.disabled = true;
    try {
      await api(`/chat/api/conversations/${activeConversation.id}/messages`, {
        method: "DELETE",
      });
      clearMessages();
      lastMessageId = 0;
      messageVersion += 1;
      await refreshConversations();
    } catch (error) {
      setError(error.message);
      elements.clearButton.disabled = false;
    }
  }

  elements.form.addEventListener("submit", sendMessage);
  elements.attachmentButton.addEventListener("click", () => elements.attachmentInput.click());
  elements.attachmentInput.addEventListener("change", updateAttachmentName);
  elements.clearButton.addEventListener("click", clearChat);
  elements.newChatButton.addEventListener("click", showUsers);
  elements.menuButton.addEventListener("click", () => elements.sidebar.classList.toggle("open"));
  elements.input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      elements.form.requestSubmit();
    }
  });
  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) poll();
  });

  refreshConversations()
    .then(() => poll())
    .catch((error) => setError(error.message));
  pollingTimer = window.setInterval(poll, 4000);

  window.addEventListener("beforeunload", () => {
    if (pollingTimer) window.clearInterval(pollingTimer);
  });
})();
