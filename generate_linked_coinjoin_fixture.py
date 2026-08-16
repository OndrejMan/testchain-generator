import argparse

from testchain.motifs.general import FinalizeChain, SetupChain
from testchain.motifs.linked_coinjoin import LinkedJoinMarketCoinjoins
from testchain.runner import Runner


parser = argparse.ArgumentParser(description="Generate the isolated linked-CoinJoin test fixture.")
parser.add_argument("--output-dir", default="../files/linked-coinjoin/", help="Fixture output directory")
parser.add_argument("--exec", default="bitcoind", help="Path to the Bitcoin Core daemon")
args = parser.parse_args()

generator = Runner(args.output_dir, "btc", args.exec)
generator.add_generator(SetupChain)
generator.add_generator(LinkedJoinMarketCoinjoins)
generator.add_generator(FinalizeChain)
generator.run()
