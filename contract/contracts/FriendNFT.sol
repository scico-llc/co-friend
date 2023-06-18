//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.18;

import "../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "../node_modules/@openzeppelin/contracts/access/Ownable.sol";
import "../node_modules/@openzeppelin/contracts/utils/Counters.sol";

contract FriendNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    constructor() ERC721("CO-friends", "COFRD") {}

    function safeMint(address to, uint256 tokenId) public onlyOwner{
        _safeMint(to, tokenId);
    }

    function _baseURI() internal view override returns (string memory)  {
        return "https://co-friend-dev.sci-co.co.jp/cofrd/metadata/";
    }
}