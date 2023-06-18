const { loadFixture } = require("@nomicfoundation/hardhat-network-helpers");
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("FriendNFT", function () {
    async function deployFixture() {
        const [owner, otherAccount] = await ethers.getSigners();

        const FriendNFT = await ethers.getContractFactory("FriendNFT");
        const friendNFT = await FriendNFT.deploy();

        return { friendNFT, owner, otherAccount };
    }

    it("Should have correct token name and symbol", async () => {
        const { friendNFT } = await loadFixture(deployFixture);

        expect(await friendNFT.name()).to.equal("CO-friends");
        expect(await friendNFT.symbol()).to.equal("COFRD");
    });

    it("Should mint a new token correctly", async () => {
        const { friendNFT, owner, otherAccount } = await loadFixture(deployFixture);

        const tokenId = 1;
        await friendNFT.connect(owner).safeMint(otherAccount.address, tokenId);
        expect(await friendNFT.ownerOf(tokenId)).to.equal(otherAccount.address);
    });

    it("Should only allow the owner to mint tokens", async () => {
        const { friendNFT, otherAccount } = await loadFixture(deployFixture);

        const tokenId = 1;
        await expect(friendNFT.connect(otherAccount).safeMint(otherAccount.address, tokenId)).to.be.revertedWith(
            "Ownable: caller is not the owner"
        )
    });

    it("Should correctly set token URI after minting", async () => {
        const { friendNFT, owner, otherAccount } = await loadFixture(deployFixture);

        const tokenId = 1;
        await friendNFT.connect(owner).safeMint(otherAccount.address, tokenId);
        const tokenURI = await friendNFT.tokenURI(tokenId);
        expect(tokenURI).to.equal("https://co-friend-dev.sci-co.co.jp/nft/metadata/1");
    });
});