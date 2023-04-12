// SPDX-License-Identifier: MIT
// SPDX License Identifier: list of commonly used licenses in free or open source documentation 

//selecting solidity version 0.8.9 
//pragma species solidity's compiler version to the compiler
pragma solidity ^0.8.3;

//Necessary Imports (I have used openzepplin framework) 
//Import Files for ERC721 
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
//Import Files to allow URI Storage
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

//code to initialize contract
//Contract is extends ERC721, ERC721URIStorage, Ownable properties
contract NFT_FCS is ERC721, ERC721URIStorage {
    //Constructor with name and symbol of the token
    constructor() ERC721("NFT_FCS", "MTK") {}

    //The function responsible for securily minting the token
    //Arguments:-
    //1. variable uri of type string, to specify the URI of the JSON file 
    //2. variable tokenId of type uint256, to specify the tokenId of token
    // the setting of this function is modified to onlyOwner 
    function safeMint(string memory uri,uint256 tokenId) public
    {
        //Mints the token 
        //Arguments Required:
        //1. msg.sender: gives address of the person calling the smart contract
        //2. tokenId
        _safeMint(msg.sender, tokenId);

        //setting URI from JSON file
        //Arguments Required:
        //1. tokenId
        //2. uri
        _setTokenURI(tokenId, uri);
    }


    //overriden this function as per documentation
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    // function to return previously set tokenURI 
    //Arguments Required:
    //1. tokenId
    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory)
    {
        return super.tokenURI(tokenId);
    }
}