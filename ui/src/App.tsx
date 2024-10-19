import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';

import Transactions from './pages/Transaction';
import Budget from './components/Budget';
import Footer from './components/Footer';
import LandingPage from './pages/LandingPage';
import LoginPage from './pages/Login';

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex flex-col min-h-screen bg-gray-900 text-gray-100">
        <Header />
        <main className="flex-grow container mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <Routes>
            <Route path="/" element={<LandingPage/>} />
            <Route path="/transactions" element={<Transactions />} />
            <Route path="/budget" element={<Budget />} />
            <Route path='/login' element={<LoginPage/>}/>
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
};

export default App;