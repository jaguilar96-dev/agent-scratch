from fakes import RecordingChatModel

from agent.application.chat_service import ChatService
from agent.domain.models import Intent
from agent.infrastructure.persistence.in_memory_store import InMemoryConversationStore


def test_returns_typed_reply_with_system_prompt_first():
    model = RecordingChatModel()
    service = ChatService(model=model, store=InMemoryConversationStore(), system_prompt="SYS", max_turns=10)

    reply = service.handle("s1", "Me robaron la tarjeta")

    assert reply.intent is Intent.SENSITIVE_ACTION
    assert [message["role"] for message in model.calls[0]] == ["system", "user"]
    assert model.calls[0][0]["content"] == "SYS"


def test_returns_typed_reply_with_system_prompt_second():
    model = RecordingChatModel()
    service = ChatService(model=model, store=InMemoryConversationStore(), system_prompt="SYS", max_turns=10)

    reply = service.handle("s2", "Quiero ver el estado de mis movimientos")

    assert reply.intent is Intent.DATA_QUERY
    assert [message["role"] for message in model.calls[0]] == ["system", "user"]
    assert model.calls[0][0]["content"] == "SYS"


def test_returns_typed_reply_with_system_prompt_third():
    model = RecordingChatModel()
    service = ChatService(model=model, store=InMemoryConversationStore(), system_prompt="SYS", max_turns=10)

    reply = service.handle("s3", "No reconozco esta operación")

    assert reply.intent is Intent.PRODUCT_QUESTION
    assert [message["role"] for message in model.calls[0]] == ["system", "user"]
    assert model.calls[0][0]["content"] == "SYS"


def test_returns_typed_reply_with_system_prompt_fourth():
    model = RecordingChatModel()
    service = ChatService(model=model, store=InMemoryConversationStore(), system_prompt="SYS", max_turns=10)

    reply = service.handle("s4", "Muy buenos días aprendiz")

    assert reply.intent is Intent.GREETING
    assert [message["role"] for message in model.calls[0]] == ["system", "user"]
    assert model.calls[0][0]["content"] == "SYS"



def test_returns_typed_reply_with_system_prompt_fifth():
    model = RecordingChatModel()
    service = ChatService(model=model, store=InMemoryConversationStore(), system_prompt="SYS", max_turns=10)

    reply = service.handle("s5", "Capital de Francia")

    assert reply.intent is Intent.OUT_OF_SCOPE
    assert [message["role"] for message in model.calls[0]] == ["system", "user"]
    assert model.calls[0][0]["content"] == "SYS"