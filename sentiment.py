
async def analyze_sentiment(comment: Dict, examples: List[Dict]) -> float:
    """分析单个评论的情感"""
    messages = [
        {"role": "system", "content": "You are a sentiment analysis assistant, specializing in analyzing comments about the game 'Black Myth: Wukong'. Please provide a sentiment score between 0 and 1, where 0 represents very negative and 1 represents very positive."},
        {"role": "user", "content": "Here are some examples:\n" + "\n".join([f"Comment: {e['comment']}\nScore: {e['score']}" for e in examples])},
        {"role": "user", "content": f"Analyze the sentiment of the following comment. Return only a float number between 0.000 and 1.000 with exactly 3 decimal places, without any additional text:\nComment: {comment['after_cleaning']}"}
    ]
    

async def main():
    # 示例数据
    examples = [
        {"comment": "I love wukong, but the difficulty is no where close to elden ring", "score": 0.665},
        {"comment": "Wukong is very good but no where near as hard as Elden Ring", "score": 0.774},
        {"comment": "The game is 85% cut scenes! Love it though", "score": 0.862},
        {"comment": "Ts is not hard bro, only reason i don't really love it as much as other", "score": 0.451},
        {"comment": "Bro I'm shocked people have completed the game already 😐😭💀", "score": 0.532},
        {"comment": "I beat Elden ring like 20 times had almost every build in the book and I have had more fun on wukong than ever on Elden ring", "score": 0.896},
        {"comment": "有没有可能第二部是黑神话：杨戬", "score": 0.802},
        {"comment": "期待后面来个dlc，三大反骨仔联手闹天宫[看]", "score": 0.903},
        {"comment": "想玩，但是家里的虎先锋不同意[流泪]", "score": 0.801},
        {"comment": "@username 妈！", "score": 0.500},
        {"comment": "只是二郎神这张翰的脸……一秒出戏[捂脸]", "score": 0.412},
        {"comment": "故事情节已有，可以拍大电影了[呲牙][呲牙]杨戬就由焦恩俊本色出演[呲牙][呲牙][呲牙]", "score": 0.819},
        {"comment": "把腾讯搬倒 才会有更多类似黑神话悟空这样的游戏重现天日 顶起来[赞][赞][赞]", "score": 0.895},
        {"comment": "跪求游戏名字[泣不成声]", "score": 0.888},
        {"comment": "Wukong just isn't what I wanted just loads of boss fights", "score": 0.200},
        {"comment": "The hole game felt like easy mode😭", "score": 0.335},
        {"comment": "这游戏就是个半成品，bug一堆，优化还差，浪费钱", "score": 0.110},
        {"comment": "画面是不错，但是剧情太烂了，完全没有代入感", "score": 0.305},
        {"comment": "黑神话：悟空，不过如此。各种缺点让人失望", "score": 0.102},
        {"comment": "最后天命人打上天庭，关键时刻杨戬出来：我来助你，那就刺激了[看]", "score": 0.957}
    ]
