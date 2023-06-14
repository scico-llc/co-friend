import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";

import network from "./networks.json";

const privateKey = process.env.PRIVATE_KEY || "0x0000000000000000000000000000000000000000000000000000000000000000"; // this is to avoid hardhat error

const config: HardhatUserConfig = {
  solidity: "0.8.13",
  networks: {
    hardhat: {
      blockGasLimit: 10000000,
    },
    rinkeby: {
      url: network.rinkeby.rpc,
      accounts: [privateKey],
    },
  }
};

export default config;
