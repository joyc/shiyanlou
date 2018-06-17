import json
import pandas as pd


def analysis(file, user_id):
    """
    从json file中统计出user_id指定用户的学习数据

    :param file: (str) json file name
    :param user_id: (int) user id
    :return: 学习次数 time 和 时间和 minutes
    """
    try:
        df = pd.read_json(file)
    except ValueError:
        return 0, 0

    df = df[df['user_id'] == user_id].minutes
    times = df.count()
    minutes = df.sum()
    # print(f'user times is: {times}\nuser minutes is: {minutes}')
    return times, minutes


def analysis_raw(file, user_id):
    """
    从file json 文件中统计出user_id中指定用户的学习数据，json模块实现
    :param file: json file name (str)
    :param user_id: user id (int)
    :return: times, minutes
    """
    times = 0
    minutes = 0

    try:
        f = open(file)
        records = json.load(f)
        for item in records:
            if item['user_id'] != user_id:
                continue
            times += 1
            minutes += item['minutes']
        f.close()
    except:
        pass
    return times, minutes


# if __name__ == '__main__':
#     analysis('user_study.json', 173927)
