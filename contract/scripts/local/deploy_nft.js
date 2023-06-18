const hre = require("hardhat");

async function main() {
  const FriendNFT = await hre.ethers.getContractFactory("FriendNFT")
  const fruendNft = await FriendNFT.deploy();
  await fruendNft.deployed();
  console.log("Deployed at: ", fruendNft.address);

  const DialyNFT = await hre.ethers.getContractFactory("DialyNFT")
  const dialyNFT = await DialyNFT.deploy();
  await dialyNFT.deployed();
  console.log("Deployed at: ", dialyNFT.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
