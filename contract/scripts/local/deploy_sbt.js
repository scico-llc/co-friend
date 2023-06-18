const hre = require("hardhat");

async function main() {
  const MemorySBT = await hre.ethers.getContractFactory("MemorySBT")
  const sbt = await MemorySBT.deploy();
  await sbt.deployed();
  console.log("Deployed at: ", sbt.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
