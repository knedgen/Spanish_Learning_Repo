from .base import BaseModel


class Score(BaseModel):
    @classmethod
    def points(self):
        return self.query("SELECT * FROM hiscores ORDER BY Points DESC, Percent DESC")
        
    @classmethod
    def percent(self):
        return self.query("SELECT * FROM hiscores ORDER BY Percent DESC, Questions DESC")
        
    @classmethod
    def questions(self):
        return self.query("SELECT * FROM hiscores ORDER BY Questions DESC, Percent DESC")