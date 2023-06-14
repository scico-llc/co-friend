//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.13;

import "../node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "../node_modules/@openzeppelin/contracts/access/Ownable.sol";
import "../node_modules/@openzeppelin/contracts/utils/Counters.sol";

contract FriendNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // 状態変数 _tokenIdConter で、ライブラリを使用できるようにする
    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("CO-friends", "COFRD") {}

    function safeMint(address to) public onlyOwner{
        // 現在のIDを取得
        uint256 tokenId = _tokenIdCounter.current();
        // インクリメント
        _tokenIdCounter.increment();
        // ミントを実行
        _safeMint(to, tokenId);
    }

    function _baseURI() internal view override returns (string memory)  {
        return "http://localhost:8080/ntt/";
    }
}