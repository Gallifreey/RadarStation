import abc

from core.library.AgentBase import AgentBase


class WorldBase(metaclass=abc.ABCMeta):
    """
    世界基类，所有的场地(虚拟/现实)均需继承此类 \n
    世界是Agent们活动的地方，Agent需要用他们的方式感知世界
    """
    def __init__(self):
        pass

    def init_state(self, states):
        """
        为世界初始化状态 \n
        :param states: 初始状态
        """
        pass

    def generate_agents(self, agents: AgentBase):
        """
        为此场景生成Agents
        :param agents: Agents
        """
        pass

    @abc.abstractmethod
    def start_main_loop(self):
        """
        开启世界主循环
        """
        pass

    @abc.abstractmethod
    def update_world(self, *args, **kwargs):
        """
        如何更新世界
        """
        pass

    @abc.abstractmethod
    def terminate_world(self, *args, **kwargs):
        """
        如何结束世界
        """
        pass

