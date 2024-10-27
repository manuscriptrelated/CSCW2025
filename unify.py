# 清洗数据，将用户名做归一化处理为@Username
import pandas as pd
import re
import os

def clean_text(text):
    if pd.isna(text):
        return text
    
    # 更新的正则表达式，采用更保守的匹配策略
    pattern = r'@[\w\u00C0-\u017F\u0400-\u04FF\u0370-\u03FF\u0590-\u05FF\u0600-\u06FF\u4e00-\u9fff\u3040-\u309F\u30A0-\u30FF★°\-_\U0001F000-\U0001F999]+'
    
    def replace_username(match):
        return '@username'
    
    # 使用替换函数来处理匹配到的用户名
    words = text.split()
    cleaned_words = []
    for word in words:
        if word.startswith('@'):
            cleaned_word = re.sub(pattern, replace_username, word)
            cleaned_words.append(cleaned_word)
        else:
            cleaned_words.append(word)
    
    return ' '.join(cleaned_words)

# 定义输入文件路径
input_file = r"discussions.csv"

# 自动生成输出文件路径，输出文件名为原文件名加上 "_cleaned"
base_name = os.path.basename(input_file)
name, ext = os.path.splitext(base_name)
output_file = os.path.join(os.path.dirname(input_file), f"{name}_cleaned{ext}")

# 读取CSV文件
df = pd.read_csv(input_file)

# 创建新的'after_cleaning'列，应用清洗函数
df['after_cleaning'] = df['text'].apply(clean_text)

# 删除'after_cleaning'列中包含空值的行
df = df.dropna(subset=['after_cleaning'])

# 保存处理后的数据到新的CSV文件
df.to_csv(output_file, index=False)

print(f"数据清洗完成，结果已保存到{output_file}")