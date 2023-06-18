require("@nomicfoundation/hardhat-toolbox");
require('dotenv').config({ path: './.env' });

const config =process.env;

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.8.18",
  defaultNetwork: "localhost",
  networks: {
    localhost: {
      url: 'http://localhost:8545',
      chainId: parseInt(config.CHAIN_ID),
    },
    mumbai: {
      url: config.NETWORK_RPC,
      chainId: parseInt(config.CHAIN_ID),
      accounts: [`${config.ADMIN_PRIVATE_KEY}`]
    }
  },
  plugins: [
  ],
  solidity: {
    compilers: [
      {
        version: '0.8.18',
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
    timeout: 120000,
  }
};
