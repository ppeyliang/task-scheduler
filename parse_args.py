import argparse
import datetime


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--url",
        help="url of the website",
        required=True
    )
    parser.add_argument(
        "-s", "--start",
        type=datetime.date.fromisoformat,
        help="start date of the task - format yyyy-mm-dd",
        required=True
    )
    parser.add_argument(
        "-e", "--end",
        type=datetime.date.fromisoformat,
        help="end date of all tasks - format yyyy-mm-dd"
    )
    parser.add_argument(
        "-wd", "--weekday",
        type=int,
        help="no. of task on weekday"
    )
    parser.add_argument(
        "-we", "--weekend",
        type=int,
        help="no. of task on weekend"
    )
    args = parser.parse_args()
    return args.url, args.start, args.end, args.weekday, args.weekend
