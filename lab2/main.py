
def count_time(artists_def, time_def, paper_amount_def):
    sections = [[] for _ in range(artists_def)]
    max_time = 0

    if artists_def == 0:
        return "Nobody is here to work"

    for i in paper_amount_def:
        min_section = min(sections, key=lambda x: sum(x))
        min_section_index = sections.index(min_section)

        if len(sections[min_section_index]) > 0:
            sections[min_section_index].append(time_def)

        sections[min_section_index].append(i * time_def)

        max_time = max(max_time, sum(sections[min_section_index]))

    return max_time


artists = 10
time = 5
paper_amount = [1, 2, 3]
result = count_time(artists, time, paper_amount)
print(result)


