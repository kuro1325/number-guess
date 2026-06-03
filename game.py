#!/usr/bin/env python3
"""猜数字游戏 - 一个简单的命令行游戏"""

import random

def main():
    print("=" * 40)
    print("     🎮 猜数字游戏")
    print("=" * 40)
    print("\n我想了一个 1-100 之间的数字，你来猜！")
    print("输入 'q' 退出游戏\n")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("你的猜测: ").strip()

        if guess.lower() == 'q':
            print(f"\n答案是 {secret}，下次再来！")
            break

        if not guess.isdigit():
            print("⚠️ 请输入数字！")
            continue

        num = int(guess)
        attempts += 1

        if num < secret:
            print("📉 太小了！")
        elif num > secret:
            print("📈 太大了！")
        else:
            print(f"\n🎉 恭喜你猜对了！答案就是 {secret}")
            print(f"🏆 你用了 {attempts} 次猜中")
            if attempts <= 5:
                print("⭐ 太厉害了！")
            elif attempts <= 10:
                print("👍 不错哦！")
            else:
                print("💪 继续加油！")
            break

    print("\n游戏结束，感谢游玩！")

if __name__ == "__main__":
    main()
