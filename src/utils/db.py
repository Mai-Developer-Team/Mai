from pymongo import MongoClient

from config import setting

cluster = MongoClient(setting.mongodb_client) 
db = cluster.maiv3


class User:
    def __init__(
        self,
        id,
        color,
        premium,
        badge,
        bio,
        xp,
        inv,
        money,
        rod,
        fish_hook,
        banner,
        contract,
        genshin_token,
        block,
        reason_block
    ):
        self.id = id
        
        self.color: str = None or color
        self.premium: len = premium
        self.badge: str = None or badge
        self.bio: str = None or bio

        self.xp: str = None or xp
        self.inv: str = None or inv
        self.money: len = None or money
        self.rod: len = None or rod
        self.fish_hook: len = None or fish_hook
        self.banner: str = None or banner
        self.contract: len = None or contract
        
        self.genshin_token: str = None or genshin_token
        self.block: len = None or block
        self.reason_block: str = None or reason_block

    
    async def insert(self) -> None:
    
        if not db.user.find_one({"id": self.id}):
            await db.user.insert_one(
                {
                    "id": self.id,
                    "profile": { 
                        "color": self.color,
                        "premium": self.premium,
                        "badge": self.badge,
                        "bio": self.bio
                    },
                    "eco": {
                        "xp": self.xp,
                        "inv": [
                            self.inv
                        ],
                        "rod": self.rod,
                        "fish_hook": self.fish_hook,
                        "banner": self.banner,
                        "contract": self.contract
                    },
                    "genshin_token": self.genshin_token,
                    "blacklist": {
                        "block": self.block,
                        "reason": self.reason_block
                    }
                }
            )

    async def delete(self) -> None:
        
        if not db.user.find_one({"id": self.id}):
            return "Чумба, ты совсем ебнулся?"
        else:
            await db.user.delete_one({"id": self.id})

    async def find(self) -> None:
        
        if not db.user.find_one({"id": self.id}):
            return "Чумба, ты совсем ебнулся?"
        else:
            return db.user.find_one({"id": self.id})
