from abc import ABC, abstractmethod


class LLMBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_prompt(self):
        raise NotImplementedError

    @abstractmethod
    def load_images(self):
        raise NotImplementedError

    @abstractmethod
    def load_model(self):
        raise NotImplementedError
