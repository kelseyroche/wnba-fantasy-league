 // vite.config.js
 import { defineConfig } from 'vite';
 import react from '@vitejs/plugin-react';

 export default defineConfig({
   plugins: [react()],
   base: '/wnba-fantasy-league/', // Set this to your repository name
 });