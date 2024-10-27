
CLASSIFICATIONS = {
    "Game Plot": "Content related to game storyline, character development, and plot discussions.",
    "Game Experience": "Player experiences, game difficulty, and progress discussions.",
    "Information Share": "Sharing game-related information such as downloads, purchases, and character details.",
    "Social Interaction": "Interactions with other users, conversations, and tagging.",
    "Game Requirement": "Users discuss the configuration needed to run properly.",
    "Audience Reaction": "Emotional reactions to game content, such as surprise, emotion, or laughter.",
    "Game Design": "Discussion of game design elements like animation, music, and art style.",
    "Progress and Updates": "Game updates, progress, and fixes.",
    "Audience Feedback": "Player feedback and evaluations of the game.",
    "Audience Anticipation": "Expectations and anticipation for future game developments."
}

async def classify_single(discussion: Dict, examples: List[Dict]) -> str:
    """Classify a single discussion"""
    messages = [
        {"role": "system", "content": "You are a classification assistant for discussions about the game 'Black Myth: Wukong'. Assign a category to each discussion based on the given examples and category descriptions."},
        {"role": "user", "content": "Here are the categories and their descriptions:\n" + "\n".join([f"{k}: {v}" for k, v in CLASSIFICATIONS.items()])},
        {"role": "user", "content": "Here are some examples:\n" + "\n".join([f"Discussion: {e['discussion']}\nClassification: {e['classification']}" for e in examples])},
        {"role": "user", "content": f"Now, please assign a category to the following discussion. Reply with the category name only:\nDiscussion: {discussion['after_cleaning']}"}
    ]


async def main():
    # 示例数据
    examples = [
        {"discussion": "The backstory of Sun Wukong is truly captivating", "classification": "Game Plot"},
        {"discussion": "游戏难度有点高，希望能调整一下", "classification": "Game Experience"},
        {"discussion": "Does anyone know when the game will be released?", "classification": "Information Share"},
        {"discussion": "What do you guys think of Wukong's new skin?", "classification": "Social Interaction"},
        {"discussion": "1060显卡可以流畅运行游戏嘛？会登录PS5平台吗", "classification": "Game Requirement"},
        {"discussion": "I jumped up with excitement when I saw Wukong transform!", "classification": "Audience Reaction"},
        {"discussion": "The art style of the game is absolutely stunning", "classification": "Game Design"},
        {"discussion": "开发团队说下个月会有重大更新", "classification": "Progress and Updates"},
        {"discussion": "The control system is a bit complex, hope they can simplify it", "classification": "Audience Feedback"},
        {"discussion": "Can't wait to see the next new character!", "classification": "Audience Anticipation"}
    ]
