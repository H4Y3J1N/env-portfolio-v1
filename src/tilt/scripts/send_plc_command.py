"""
PLC Command Script

Send tilt commands to PLC controller.

Usage:
    python send_plc_command.py --angle 45.0
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description='Send PLC tilt command')
    parser.add_argument('--angle', type=float, required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    print(f"PLC command script skeleton - Angle: {args.angle}")


if __name__ == '__main__':
    main()
