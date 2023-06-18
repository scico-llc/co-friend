require("@nomicfoundation/hardhat-toolbox");
require('dotenv').config({ path: './.env' });

const config =process.env;

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  defaultNetwork: "localhost",
  networks: {
    localhost: {
      url: 'http://localhost:8545',
      chainId: config.CHAIN_ID,
    },
    testnet: {
      url: config.NETWORK_RPC,
      chainId: parseInt(config.CHAIN_ID),
      accounts: config.ADMIN_PRIVATE_KEY ? [config.ADMIN_PRIVATE_KEY] : []
    }
  },
  plugins: [
  ],
  solidity: {
    compilers: [
      {
        version: '0.8.19',
        settings: {
          optimizer: {
            enabled: true,
            runs: 200,
          },
        },
      },
    ],
  },
  paths: {
    sources: './contracts',
    tests: './test',
    cache: './cache',
    artifacts: './artifacts',
  },
  mocha: {
    timeout: 40000,
  }
};

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.18",
};
