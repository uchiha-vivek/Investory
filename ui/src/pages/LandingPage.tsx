import React, { ReactNode } from 'react';
import { Link } from 'react-router-dom';
import { ChartBarIcon, CreditCardIcon } from 'lucide-react';

interface FeatureCardProps {
  icon: ReactNode; // JSX element like icons
  title: string;
  description: string;
}

const LandingPage: React.FC = () => {
  return (
    <div className="bg-gray-900 text-gray-100 min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-b from-gray-800 to-gray-900 py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">Take Control of Your Finances</h1>
          <p className="text-xl md:text-2xl mb-8">Simplify your budget, track expenses, and achieve your financial goals.</p>
          <Link to="/signup" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full text-lg transition duration-300">
            Get Started for Free
          </Link>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12">Key Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <FeatureCard
              icon={<ChartBarIcon className="w-12 h-12" />}
              title="Insightful Analytics"
              description="Gain valuable insights into your spending habits and financial trends."
            />
            <FeatureCard
              icon={<CreditCardIcon className="w-12 h-12" />}
              title="Expense Tracking"
              description="Easily categorize and monitor your expenses in real-time."
            />
            <FeatureCard
              icon={<ChartBarIcon className="w-12 h-12" />}
              title="Budget Planning"
              description="Create and manage budgets to stay on top of your financial goals."
            />
            <FeatureCard
              icon={<ChartBarIcon className="w-12 h-12" />}
              title="Fast & Secure"
              description="Bank-level encryption keeps your financial data safe and secure."
            />
          </div>
        </div>
      </section>

      {/* Testimonial Section */}
      <section className="bg-gray-800 py-16">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-8">What Our Users Say</h2>
          <blockquote className="text-xl italic mb-4">
            "This app has completely transformed how I manage my finances. It's intuitive, powerful, and has helped me save more than ever before."
          </blockquote>
          <p className="font-semibold">- Sarah J., Small Business Owner</p>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-6">Ready to Take Control?</h2>
          <p className="text-xl mb-8">Join thousands of users who have improved their financial health with our app.</p>
          <Link to="/signup" className="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-full text-lg transition duration-300">
            Start Your Free Trial
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-gray-300 py-8">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2024 Finance App. All rights reserved.</p>
          <div className="mt-4 space-x-4">
            <a href="#" className="hover:text-blue-400">Privacy Policy</a>
            <a href="#" className="hover:text-blue-400">Terms of Service</a>
            <a href="#" className="hover:text-blue-400">Contact Us</a>
          </div>
        </div>
      </footer>
    </div>
  );
};

const FeatureCard: React.FC<FeatureCardProps> = ({ icon, title, description }) => (
  <div className="bg-gray-800 p-6 rounded-lg text-center">
    <div className="text-blue-500 mb-4">{icon}</div>
    <h3 className="text-xl font-semibold mb-2">{title}</h3>
    <p className="text-gray-400">{description}</p>
  </div>
);

export default LandingPage;
