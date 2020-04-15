import matplotlib.pyplot as plt

if __name__ == '__main__':
    four_byte_words_ops_per_word = []

    mflops_normal = []
    with open('OpenMPLog_normal.txt', 'r') as f_normal:
        lines_normal = f_normal.readlines()
        for line in lines_normal[22:25]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            four_byte_words_ops_per_word.append(elements[4] + ' - ' + elements[5])
            mflops_normal.append(int(elements[8]))
        for line in lines_normal[26:29]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            four_byte_words_ops_per_word.append(elements[4] + ' - ' + elements[5])
            mflops_normal.append(int(elements[8]))
        for line in lines_normal[30:33]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            four_byte_words_ops_per_word.append(elements[4] + ' - ' + elements[5])
            mflops_normal.append(int(elements[8]))

    mflops_openmp = []
    with open('OpenMPLog_openmp.txt', 'r') as f_openmp:
        lines_openmp = f_openmp.readlines()
        for line in lines_openmp[22:25]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            mflops_openmp.append(int(elements[8]))
        for line in lines_openmp[26:29]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            mflops_openmp.append(int(elements[8]))
        for line in lines_openmp[30:33]:
            elements = list(filter(lambda a: a != '', line.strip().split(' ')))
            mflops_openmp.append(int(elements[8]))

    fig = plt.figure(figsize=(14, 10))
    fig.subplots_adjust(bottom=0.2)
    triad_three_types = fig.add_subplot(111)
    triad_three_types.plot(four_byte_words_ops_per_word, mflops_normal, 'bo-', label='normal')
    triad_three_types.plot(four_byte_words_ops_per_word, mflops_openmp, 'rs-', label='openmp')
    triad_three_types.set_xlabel('four byte words - ops (triad operations) per word', labelpad=15)
    triad_three_types.set_ylabel('MFLOPS')
    triad_three_types.set_title('Triad operations', loc='center', fontweight='bold')
    handles, labels = triad_three_types.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center')
    plt.savefig('triad_3_types_64.png', bbox_inches='tight')
    plt.show()