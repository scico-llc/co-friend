const hre = require("hardhat");

async function main() {
    const FriendNFT = await hre.ethers.getContractFactory("FriendNFT")
    const nft = await FriendNFT.deploy();
    await nft.deployed();
    console.log("FriendNFT Deployed at: ", nft.address);

    const DialyNFT = await hre.ethers.getContractFactory("DialyNFT")
    const dialyNFT = await DialyNFT.deploy();
    await dialyNFT.deployed();
    console.log("DialyNFT Deployed at: ", dialyNFT.address);

    const MemorySBT = await hre.ethers.getContractFactory("MemorySBT")
    const sbt = await MemorySBT.deploy();
    await sbt.deployed();
    console.log("MemorySBT Deployed at: ", sbt.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
