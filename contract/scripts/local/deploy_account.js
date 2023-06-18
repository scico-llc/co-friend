const hre = require("hardhat");

async function main() {
    const CCExecutorList = await hre.ethers.getContractFactory("CrossChainExecutorList");
    const ccExecutorList = await CCExecutorList.deploy();
    await ccExecutorList.deployed();
    console.log("CCExecutorList Deployed at: ", ccExecutorList.address);
    
    const Account = await hre.ethers.getContractFactory("Account");
    const account = await Account.deploy(ccExecutorList.address);
    await account.deployed();
    console.log("Account Deployed at: ", account.address);
    
    const AccountRegistry = await hre.ethers.getContractFactory("AccountRegistry");
    const accountRegistry = await AccountRegistry.deploy(account.address);
    await accountRegistry.deployed();
    console.log("AccountRegistry Deployed at: ", accountRegistry.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
