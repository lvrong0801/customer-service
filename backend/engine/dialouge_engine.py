from domain.message import UserMessage
from domain.state import DialogueState


class DialogueEngine:

    async def process_message(self,state:DialogueState,user_message:UserMessage):
        pass