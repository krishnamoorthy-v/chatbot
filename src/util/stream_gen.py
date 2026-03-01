from typing import AsyncIterator, Any
import logging


class AsyncGen:
    def __init__(self, stream: AsyncIterator[Any]):
        self._stream = stream
        self.input_token = 0
        self.output_token = 0
        self.total_token = 0

    async def run(self) -> AsyncIterator[str]:
        try:
            async for chunk in self._stream:
                msg = chunk[0] if isinstance(chunk, (list, tuple)) else chunk

                usage = getattr(msg, "usage_metadata", None) or {}

                self.input_token += usage.get("input_tokens", 0)
                self.output_token += usage.get("output_tokens", 0)
                self.total_token += usage.get("total_tokens", 0)

                content = getattr(msg, "content", None)
                if content:
                    yield content

        except Exception:
            logging.exception("Streaming error")
            raise  # re-raise original exception correctly
