from openai import OpenAI

from agent.domain.models import AgentReply, Message
from agent.infrastructure.llm.credentials import Credential


class FoundryChatModel:
    """Implementa el puerto ChatModel contra Microsoft Foundry."""

    def __init__(
        self,
        endpoint: str,
        credential: Credential,
        deployment: str,
        timeout_s: float,
        max_retries: int,
    ) -> None:
        self.client = OpenAI(
            base_url=f"{endpoint.rstrip('/')}/openai/v1/",
            api_key=credential,
            timeout=timeout_s,
            max_retries=max_retries,
        )
        self.deployment = deployment

    def complete(self, messages: list[Message]) -> AgentReply:
        # TODO S2: medir latencia y tokens; traducir timeout, 429,
        # salida inválida y errores de Foundry a AgentError del dominio.

        completion = self.client.chat.completions.parse(
            model=self.deployment,
            messages=messages,
            response_format=AgentReply,
        )

        message = completion.choices[0].message

        if message.parsed is None:
            raise RuntimeError(
                f"El modelo no devolvió el contrato: {message.refusal or 'vacío'}"
            )

        return message.parsed

    # TODO S2: medir latencia y tokens; traducir errores
    # de Foundry a AgentError del dominio.
