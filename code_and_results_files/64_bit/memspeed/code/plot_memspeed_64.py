import matplotlib.pyplot as plt

if __name__ == '__main__':
    memory = []

    double_triad_normal = []
    single_triad_normal = []
    int_triad_normal = []
    double_add_normal = []
    single_add_normal = []
    int_add_normal = []
    double_assign_normal = []
    single_assign_normal = []
    int_assign_normal = []
    with open('memSpeed_normal.txt', 'r') as f_normal:
        lines_normal = f_normal.readlines()[23:44]
        for line in lines_normal[:-1]:
            for iterator, element in enumerate(list(filter(lambda a: a != '', line.strip().split(' ')))):
                if iterator % 10 == 0:
                    memory.append(element)
                elif iterator % 10 == 1:
                    double_triad_normal.append(float(element) / 8)
                elif iterator % 10 == 2:
                    single_triad_normal.append(float(element) / 4)
                elif iterator % 10 == 3:
                    int_triad_normal.append(float(element) * 11 / 8)
                elif iterator % 10 == 4:
                    double_assign_normal.append(float(element) / 8)
                elif iterator % 10 == 5:
                    single_assign_normal.append(float(element) / 4)
                elif iterator % 10 == 6:
                    int_assign_normal.append(float(element) * 11 / 8)
                elif iterator % 10 == 7:
                    double_add_normal.append(float(element) / 8)
                elif iterator % 10 == 8:
                    single_add_normal.append(float(element) / 4)
                else:
                    int_add_normal.append(float(element) * 11 / 8)

    double_triad_openmp = []
    single_triad_openmp = []
    int_triad_openmp = []
    double_add_openmp = []
    single_add_openmp = []
    int_add_openmp = []
    double_assign_openmp = []
    single_assign_openmp = []
    int_assign_openmp = []
    with open('memSpeed_openmp.txt', 'r') as f_openmp:
        lines_openmp = f_openmp.readlines()[23:44]
        for line in lines_openmp[:-1]:
            for iterator, element in enumerate(list(filter(lambda a: a != '', line.strip().split(' ')))):
                if iterator % 10 == 1:
                    double_triad_openmp.append(float(element) / 8)
                elif iterator % 10 == 2:
                    single_triad_openmp.append(float(element) / 4)
                elif iterator % 10 == 3:
                    int_triad_openmp.append(float(element) * 11 / 8)
                elif iterator % 10 == 4:
                    double_assign_openmp.append(float(element) / 8)
                elif iterator % 10 == 5:
                    single_assign_openmp.append(float(element) / 4)
                elif iterator % 10 == 6:
                    int_assign_openmp.append(float(element) * 11 / 8)
                elif iterator % 10 == 7:
                    double_add_openmp.append(float(element) / 8)
                elif iterator % 10 == 8:
                    single_add_openmp.append(float(element) / 4)
                elif iterator % 10 == 9:
                    int_add_openmp.append(float(element) * 11 / 8)

    fig = plt.figure(figsize=(14, 10))
    fig.subplots_adjust(bottom=0.35, wspace=0.4)
    double_triad_plot = fig.add_subplot(131)
    double_triad_plot.plot(memory, double_triad_normal, 'bo-', label='double triad normal')
    double_triad_plot.plot(memory, double_triad_openmp, 'rs-', label='double triad openmp')
    double_triad_plot.set_xlabel('Memory Kbytes used')
    double_triad_plot.set_xticklabels(memory, rotation=(90))
    double_triad_plot.set_ylabel('MFLOPS')
    double_triad_plot.set_title('Triad operation', loc='center', fontweight='bold')
    double_add_plot = fig.add_subplot(132)
    double_add_plot.plot(memory, double_add_normal, 'g^-', label='double add normal')
    double_add_plot.plot(memory, double_add_openmp, 'yx-', label='double add openmp')
    double_add_plot.set_xlabel('Memory Kbytes used')
    double_add_plot.set_xticklabels(memory, rotation=(90))
    double_add_plot.set_ylabel('MFLOPS')
    double_add_plot.set_title('Add operation', loc='center', fontweight='bold')
    double_assign_plot = fig.add_subplot(133)
    double_assign_plot.plot(memory, double_assign_normal, 'cv-', label='double assign normal')
    double_assign_plot.plot(memory, double_assign_openmp, 'md-', label='double assign openmp')
    double_assign_plot.set_xlabel('Memory Kbytes used')
    double_assign_plot.set_xticklabels(memory, rotation=(90))
    double_assign_plot.set_ylabel('MFLOPS')
    double_assign_plot.set_title('Assign operation', loc='center', fontweight='bold')
    handles, labels = double_triad_plot.get_legend_handles_labels()
    handles += double_add_plot.get_legend_handles_labels()[0]
    labels += double_add_plot.get_legend_handles_labels()[1]
    handles += double_assign_plot.get_legend_handles_labels()[0]
    labels += double_assign_plot.get_legend_handles_labels()[1]
    fig.legend(handles, labels, loc='lower center')
    plt.savefig('double_64_bit.png', bbox_inches='tight')
    plt.show()

    fig = plt.figure(figsize=(14, 10))
    fig.subplots_adjust(bottom=0.35, wspace=0.4)
    single_triad_plot = fig.add_subplot(131)
    single_triad_plot.plot(memory, single_triad_normal, 'bo-', label='single triad normal')
    single_triad_plot.plot(memory, single_triad_openmp, 'rs-', label='single triad openmp')
    single_triad_plot.set_xlabel('Memory Kbytes used')
    single_triad_plot.set_xticklabels(memory, rotation=(90))
    single_triad_plot.set_ylabel('MFLOPS')
    single_triad_plot.set_title('Triad operation', loc='center', fontweight='bold')
    single_add_plot = fig.add_subplot(132)
    single_add_plot.plot(memory, single_add_normal, 'g^-', label='single add normal')
    single_add_plot.plot(memory, single_add_openmp, 'yx-', label='single add openmp')
    single_add_plot.set_xlabel('Memory Kbytes used')
    single_add_plot.set_xticklabels(memory, rotation=(90))
    single_add_plot.set_ylabel('MFLOPS')
    single_add_plot.set_title('Add operation', loc='center', fontweight='bold')
    single_assign_plot = fig.add_subplot(133)
    single_assign_plot.plot(memory, single_assign_normal, 'cv-', label='single assign normal')
    single_assign_plot.plot(memory, single_assign_openmp, 'md-', label='single assign openmp')
    single_assign_plot.set_xlabel('Memory Kbytes used')
    single_assign_plot.set_xticklabels(memory, rotation=(90))
    single_assign_plot.set_ylabel('MFLOPS')
    single_assign_plot.set_title('Assign operation', loc='center', fontweight='bold')
    handles, labels = single_triad_plot.get_legend_handles_labels()
    handles += single_add_plot.get_legend_handles_labels()[0]
    labels += single_add_plot.get_legend_handles_labels()[1]
    handles += single_assign_plot.get_legend_handles_labels()[0]
    labels += single_assign_plot.get_legend_handles_labels()[1]
    fig.legend(handles, labels, loc='lower center')
    plt.savefig('single_64_bit.png', bbox_inches='tight')
    plt.show()

    fig = plt.figure(figsize=(14, 10))
    fig.subplots_adjust(bottom=0.35, wspace=0.4)
    int_triad_plot = fig.add_subplot(131)
    int_triad_plot.plot(memory, int_triad_normal, 'bo-', label='int triad normal')
    int_triad_plot.plot(memory, int_triad_openmp, 'rs-', label='int triad openmp')
    int_triad_plot.set_xlabel('Memory Kbytes used')
    int_triad_plot.set_xticklabels(memory, rotation=(90))
    int_triad_plot.set_ylabel('MFLOPS')
    int_triad_plot.set_title('Triad operation', loc='center', fontweight='bold')
    int_add_plot = fig.add_subplot(132)
    int_add_plot.plot(memory, int_add_normal, 'g^-', label='int add normal')
    int_add_plot.plot(memory, int_add_openmp, 'yx-', label='int add openmp')
    int_add_plot.set_xlabel('Memory Kbytes used')
    int_add_plot.set_xticklabels(memory, rotation=(90))
    int_add_plot.set_ylabel('MFLOPS')
    int_add_plot.set_title('Add operation', loc='center', fontweight='bold')
    int_assign_plot = fig.add_subplot(133)
    int_assign_plot.plot(memory, int_assign_normal, 'cv-', label='int assign normal')
    int_assign_plot.plot(memory, int_assign_openmp, 'md-', label='int assign openmp')
    int_assign_plot.set_xlabel('Memory Kbytes used')
    int_assign_plot.set_xticklabels(memory, rotation=(90))
    int_assign_plot.set_ylabel('MFLOPS')
    int_assign_plot.set_title('Assign operation', loc='center', fontweight='bold')
    handles, labels = int_triad_plot.get_legend_handles_labels()
    handles += int_add_plot.get_legend_handles_labels()[0]
    labels += int_add_plot.get_legend_handles_labels()[1]
    handles += int_assign_plot.get_legend_handles_labels()[0]
    labels += int_assign_plot.get_legend_handles_labels()[1]
    fig.legend(handles, labels, loc='lower center')
    plt.savefig('int_64_bit.png', bbox_inches='tight')
    plt.show()