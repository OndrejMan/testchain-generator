from testchain.runner import Generator


class LinkedJoinMarketCoinjoins(Generator):

    def run(self):
        funding_values = [0.20, 0.21, 0.22, 0.23, 0.24]
        sources = [self.next_address("p2wpkh") for _ in funding_values]
        for source, value in zip(sources, funding_values):
            self.fund_address(source, value)
        self.generate_block(1)

        first_mix_outputs = [self.next_address("p2wpkh") for _ in range(5)]
        first_change_outputs = [self.next_address("p2wpkh") for _ in range(5)]
        first_output_values = [0.10] * 5 + [0.09, 0.11, 0.12, 0.13, 0.1499]
        for output, value in zip(first_mix_outputs + first_change_outputs, first_output_values):
            output.value = value
        first_txid = self.create_transaction(sources, first_mix_outputs + first_change_outputs, first_output_values)
        self.generate_block(1)

        second_mix_outputs = [self.next_address("p2wpkh") for _ in range(5)]
        second_change_outputs = [self.next_address("p2wpkh") for _ in range(5)]
        second_output_values = [0.07] * 5 + [0.01, 0.02, 0.03, 0.04, 0.0499]
        for output, value in zip(second_mix_outputs + second_change_outputs, second_output_values):
            output.value = value
        second_txid = self.create_transaction(
            first_mix_outputs, second_mix_outputs + second_change_outputs, second_output_values)
        self.generate_block(1)

        self.log_value("linked-joinmarket-first-tx", first_txid)
        self.log_value("linked-joinmarket-second-tx", second_txid)
