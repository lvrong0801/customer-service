from dataclasses import dataclass, field

from domain.message import UserMessage, BotMessage


@dataclass
class Turn:
    turn_id:str
    user_message:UserMessage
    bot_messages: list[BotMessage] =field(default_factory=list)


@dataclass
class Session:
    session_id:str
    started_at:float
    last_activity_at:float
    closed_at:float | None = None
    turns:list[Turn] = field(default_factory=list)


@dataclass
class FocusedObject:
    type:str
    id:str
    title:str | None =None
    attributes:dict = field(default_factory=dict)


@dataclass
class SharedState:
    focused_object:FocusedObject | None =None
    session:list[Session] = field(default_factory=list)


@dataclass
class TaskInstance:
    flow_id:str
    step_id:str | None
    task_id: str
    slots:dict = field(default_factory=dict)


@dataclass
class TaskState:
    active:TaskInstance | None = None
    paused:list[TaskInstance] = field(default_factory=list)


@dataclass
class DialogueState:
    sender_id:str
    shared_state:SharedState = field(default_factory=SharedState)
    task_state:TaskState = field(default_factory=TaskState)

