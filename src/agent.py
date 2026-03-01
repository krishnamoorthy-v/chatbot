from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
import dotenv

dotenv.load_dotenv()

_limiter_grok_4_1_fast_reasoning = InMemoryRateLimiter(requests_per_second=480 / 60)
_model = init_chat_model(model="grok-4-1-fast-reasoning", model_provider="xai", temperature=1.0, max_tokens=1300,
                         max_retries=2, timeout=10, rate_limiter=_limiter_grok_4_1_fast_reasoning)


def assistant_agent(tool=None) -> create_agent:
    if tool is None:
        tool = []
    agent = create_agent(model=_model, system_prompt="you are a personal assistant", tools=tool)
    return agent
