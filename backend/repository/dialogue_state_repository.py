from pydantic import TypeAdapter
from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from domain.state import DialogueState
from models.dialogue_state import DialogueStateRecord


DIALOGUE_STATE_ADAPTER = TypeAdapter(DialogueState)


class DialogueStateRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def load_state(
            self,
            sender_id: str,
    ) -> DialogueState:
        statement = select(DialogueStateRecord).where(
            DialogueStateRecord.sender_id == sender_id
        )
        result = await self.session.execute(statement)
        record = result.scalar_one_or_none()

        if record is None:
            return DialogueState(sender_id=sender_id)

        return DIALOGUE_STATE_ADAPTER.validate_json(
            record.state_json
        )

    async def save_state(
            self,
            state: DialogueState,
    ) -> None:
        state_json = DIALOGUE_STATE_ADAPTER.dump_json(
            state
        ).decode("utf-8")

        statement = insert(DialogueStateRecord).values(
            sender_id=state.sender_id,
            state_json=state_json,
        )
        statement = statement.on_duplicate_key_update(
            state_json=statement.inserted.state_json
        )

        await self.session.execute(statement)
        await self.session.commit()