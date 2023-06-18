const {default: Web3} = require("web3");

const CONTRACT_ADDRESS = "0x0165878A594ca255338adfa4d48449f69242Eb8F";
const PUBLIC_KEY = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266";
const PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
const TARGET_KEY="0x70997970C51812dc3A010C7d01b50e0d17dc79C8"
const PROVIDER_URL = "http://localhost:8545";


async function mintNFT() {
    const web3 = new Web3(PROVIDER_URL);
    const contract = require("../artifacts/contracts/FriendNFT.sol/FriendNFT.json");
    const nftContract = new web3.eth.Contract(contract.abi, CONTRACT_ADDRESS);
    const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, "latest");
    const tx = {
        from: PUBLIC_KEY,
        to: CONTRACT_ADDRESS,
        nonce: nonce,
        gas: 500000,
        gasPrice: 401880840,
        data: nftContract.methods.safeMint(TARGET_KEY).encodeABI(),
    };

    const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    signPromise
        .then((signedTx) => {
            const tx = signedTx.rawTransaction;
            if( tx !== undefined ){
                web3.eth.sendSignedTransaction(tx, function(err, hash) {
                    if( !err ) {
                        console.log("The hash of your transaction is:", hash);
                    } else {
                        console.log("Something went wrong when submittion your transaction:", err);
                    }
                });
            }
            console.log("row36");
        })
        .catch( (err) => {
            console.log("Promise failed:", err);
        });
}

mintNFT();