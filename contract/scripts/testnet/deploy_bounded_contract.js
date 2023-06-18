const hre = require("hardhat");

async function main() {
  const DialyNFT = await hre.ethers.getContractFactory("DialyNFT")
  const dialyNFT = await DialyNFT.deploy();
  await dialyNFT.deployed();
  console.log("Deployed at: ", dialyNFT.address);

  const MemorySBT = await hre.ethers.getContractFactory("MemorySBT")
  const sbt = await MemorySBT.deploy();
  await sbt.deployed();
  console.log("MemorySBT Deployed at: ", sbt.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
