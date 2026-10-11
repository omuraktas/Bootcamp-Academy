def calculate_total_score(*scores):
    total = 0

    for score in scores:
        total += score

    return total


def calculate_success_rate(completed_lessons, total_lessons):
    if total_lessons == 0:
        return 0

    return (completed_lessons / total_lessons) * 100


def calculate_level(score):
    if score < 50:
        return "Başlangıç"
    elif score < 150:
        return "Orta"
    elif score < 300:
        return "İyi"
    else:
        return "Uzman"