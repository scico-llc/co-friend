const hre = require("hardhat");

async function main() {
  const FriendNFT = await hre.ethers.getContractFactory("FriendNFT")
  const nft = await FriendNFT.deploy();
  await nft.deployed();
  console.log("Deployed at: ", nft.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
