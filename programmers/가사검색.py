import bisect


def solution(words, queries):
    answer = []
    word_len_dict = {}
    word_len_dict_reverse = {}
    for w in words:
        if len(w) not in word_len_dict:
            word_len_dict[len(w)] = [w]
            word_len_dict_reverse[len(w)] = [w[::-1]]
        else:
            word_len_dict[len(w)].append(w)
            word_len_dict_reverse[len(w)].append(w[::-1])
    for key in word_len_dict.keys():
        word_len_dict[key].sort()
        word_len_dict_reverse[key].sort()

    for q in queries:
        l = len(q)
        if l not in word_len_dict.keys():
            answer.append(0)
            continue
        if q[0] != "?":
            left_str = q.replace("?", "a")
            right_str = q.replace("?", "z")
            l_idx = bisect.bisect_left(word_len_dict[l], left_str)
            r_idx = bisect.bisect_right(word_len_dict[l], right_str)
            answer.append(r_idx - l_idx)
        else:
            left_str = q[::-1].replace("?", "a")
            right_str = q[::-1].replace("?", "z")
            l_idx = bisect.bisect_left(word_len_dict_reverse[l], left_str)
            r_idx = bisect.bisect_right(word_len_dict_reverse[l], right_str)
            answer.append(r_idx - l_idx)
    return answer


print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"],
    )
)
