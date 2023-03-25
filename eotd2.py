from eotd2.models import Zombi, Zombis
from eotd2.models import Market

def main():
    market = Market()
    market.complete_stall()
    for tool in market.stall:
        print(tool)

if __name__ == "__main__":
    main()