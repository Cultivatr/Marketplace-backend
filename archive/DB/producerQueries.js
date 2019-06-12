const pool = require('../connection');

//make this a real function
ifSecuredUser = async (token) => {
	return 1;
};

const getOfferedItemByUserId = async(request, response) => {
    let user_id = 1;
    let queryText = `SELECT * FROM OFFERED_ITEM WHERE USER_ID = ${user_id};`
    
    const offered_items = await pool.query(queryText, function (error, results) {
        ifSecuredUser(request).then((securedUser) => {
            if (error) {
                throw error;
            }
            return (response.status(200).json(results.rows))
        })
    })
};

// const addOfferedItemByUserId = (req, res, data) => {
//     let queryText = ``

//     pool.query(queryText, function (error, results) {
//         ifSecuredUser(req).then((securedUser) => {
//             let data = {
//                 user_id: securedUser,
//                 breed: req.body.breed,
//                 type_of_feed: req.body.type_of_feed
//             };
//             if (error) {
//                 throw error;
//             }
//             res.status(200).json(results.rows);
//         })
//     })
// };

// const addEntryForStatusTrackerByOfferId = (req, res, item_id) => {
//     let queryText = ``

//     pool.query(queryText, function (error, results) {
//         ifSecuredUser(req).then((securedUser) => {
//             if (error) {
//                 throw error;
//             }
//             res.status(200).json(results.rows);
//         })
//     })
// }
    
module.exports = { 
    getOfferedItemByUserId, 
    // addOfferedItemByUserId, 
    // addEntryForStatusTrackerByOfferId,
};