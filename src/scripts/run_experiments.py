import argparse
import sys
from pathlib import Path

# Cho phep chay script truc tiep tu bat ky thu muc nao bang cach
# them thu muc goc cua project vao sys.path.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.experiments.parameter_experiment import run_experiment  # noqa: E402


def parse_threshold_pair(value):
    """
    Chuyen chuoi dang "low:high" thanh tuple (int, int).

    Vi du: "100:200" -> (100, 200)
    """

    try:
        low_str, high_str = value.split(":")
        return int(low_str), int(high_str)
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Threshold phai co dinh dang low:high, "
            f"vi du 100:200. Nhan duoc: {value}"
        )


def build_parser():
    """Tao argparse.ArgumentParser cho script."""

    parser = argparse.ArgumentParser(
        description=(
            "TV5 - Parameter Experiment: thu nghiem anh huong cua "
            "Sigma va Threshold den ket qua Canny Edge Detection."
        )
    )

    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help=(
            "Duong dan anh dau vao. Neu khong chi dinh, script se tu "
            "dong tim anh trong data/input/normal/ hoac tao anh mau."
        )
    )

    parser.add_argument(
        "--sigma",
        type=float,
        nargs="+",
        default=None,
        metavar="SIGMA",
        help="Danh sach gia tri sigma can thu nghiem (vd: --sigma 0.5 1 2)."
    )

    parser.add_argument(
        "--thresholds",
        type=parse_threshold_pair,
        nargs="+",
        default=None,
        metavar="LOW:HIGH",
        help=(
            "Danh sach cap threshold can thu nghiem, dinh dang low:high "
            "(vd: --thresholds 50:100 100:200 150:300)."
        )
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    run_experiment(
        input_path=args.input,
        sigma_values=args.sigma,
        threshold_pairs=args.thresholds
    )


if __name__ == "__main__":
    main()
