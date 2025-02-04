// import axios from 'axios';

//    const api = axios.create({
//      baseURL: 'http://localhost:5555', // Your Flask server URL
//      withCredentials: true, // Include credentials for cross-origin requests if needed
//    });

//    export default api;


   import axios from 'axios';

   const api = axios.create({
     baseURL: 'http://localhost:5555', // Your Flask server URL
     withCredentials: true, // Include credentials for cross-origin requests if needed
   });

   export { api }; // Named export