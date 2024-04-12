from . import Application


class Cut(Application.Application):
    def exec(self, args, input, output):
        file = input

        if len(args) < 2:
            raise ValueError("wrong number of command line arguments")

        if args[0] != "-b":
            raise ValueError("Must start with an option")

        if len(args) == 3:
            file = open(args[2])

        longest_line = left = right = -1
        intervals = args[1].split(',')
        lines = []

        for line in file:
            line = line.strip('\n')
            longest_line = max(longest_line, len(line))
            lines.append(line)

        cut = [False for _ in range(longest_line)]

        for i, interval in enumerate(intervals):
            if interval[0] == '-':
                intervals[i] = f'1{interval}'
            if interval[len(interval) - 1] == '-':
                intervals[i] = f'{interval}{longest_line}'

        for interval in intervals:
            split = interval.split('-')
            if len(split) == 1:
                left = right = int(split[0]) - 1
            else:
                left, right = int(split[0]) - 1, int(split[1]) - 1

            for i in range(left, right + 1):
                cut[i] = True

        for line in lines:
            line_to_write = ''.join(c for i, c in enumerate(line)
                                    if i < len(line) and cut[i])
            output.write(line_to_write + "\n")
