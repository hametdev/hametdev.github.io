import React from 'react';

export function AufixPrivacyPolicy() {
  return (
    <div className="min-h-screen bg-white text-gray-900 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-8">Privacy Policy for Aufix</h1>
        
        <p className="mb-4"><strong>Last updated:</strong> January 14, 2026</p>
        
        <p className="mb-6">
          This Privacy Policy describes how <strong>Aufix</strong> ("we", "our", or "us") collects, uses, and protects your information when you use our mobile application (the "App"). We demand the highest standards for data privacy and security.
        </p>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">1. Information We Collect</h2>
          <p className="mb-4">
            We collect only the minimum amount of information necessary to provide the App's functionality.
          </p>

          <h3 className="text-xl font-semibold mb-3">A. Personal Information (Account Data)</h3>
          <p className="mb-4">To create an account and sync your data across devices, we collect:</p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Email Address:</strong> Used solely for authentication (logging in) and password recovery.
            </li>
            <li className="mb-2">
              <strong>Password:</strong> Encrypted and handled securely. We do not have access to your raw password; it is processed via secure authentication providers (e.g., Google Firebase Auth).
            </li>
          </ul>

          <h3 className="text-xl font-semibold mb-3">B. User-Generated Content</h3>
          <p className="mb-4">
            To provide the core functionality of expense tracking, we store the following data on our secure servers:
          </p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Expense Records:</strong> The list of car-related expenses you input.
            </li>
            <li className="mb-2">
              <strong>Images:</strong> Car icons and user avatars that you choose to upload.
            </li>
          </ul>

          <h3 className="text-xl font-semibold mb-3">C. Device Permissions</h3>
          <p className="mb-4">
            The App may request access to specific features on your device. You can grant or deny these permissions at any time.
          </p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Camera & Photo Library:</strong>
              <ul className="list-disc pl-6 mt-2">
                <li className="mb-1">
                  <strong>Why we use it:</strong> This permission is required <strong>strictly</strong> to allow you to take a photo of your vehicle for the car icon or to set a user profile picture.
                </li>
                <li className="mb-1">
                  <strong>Data Handling:</strong> Photos taken for these purposes are stored as part of your profile. We do not use the camera for any other purpose and do not access your photo library without your explicit action.
                </li>
              </ul>
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">2. How We Store Your Data</h2>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Local Storage:</strong> We prioritize keeping your personal usage data on your device whenever possible for speed and privacy.
            </li>
            <li className="mb-2">
              <strong>Cloud Storage:</strong> Essential data required for synchronization (Expense lists, Car profiles, Avatars) is stored in a secure cloud database (Google Firebase).
            </li>
            <li className="mb-2">
              <strong>Security:</strong> We implement industry-standard security measures to protect your data from unauthorized access.
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">3. Subscriptions and Payments</h2>
          <p className="mb-4">We offer paid subscriptions (Premium features).</p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Payment Processing:</strong> We <strong>do not</strong> collect or store your credit card information or billing details. All financial transactions are handled exclusively by <strong>Google Play Store</strong> (Android) or <strong>Apple App Store</strong> (iOS).
            </li>
            <li className="mb-2">
              <strong>Subscription Management:</strong> We use <strong>RevenueCat</strong>, a secure third-party service, to validate your subscription status. We share only an anonymous App User ID with RevenueCat to functionality check if you have an active "Pro" plan.
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">4. Data Sharing and Third Parties</h2>
          <p className="mb-4">
            <strong>We do not sell, trade, or rent your personal identification information to others.</strong>
          </p>
          <p className="mb-4">
            We may use trusted third-party service providers solely to help us operate the App:
          </p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>Google Firebase:</strong> For secure authentication and database storage.
            </li>
            <li className="mb-2">
              <strong>RevenueCat:</strong> For managing subscription status.
            </li>
          </ul>
          <p className="mb-4">
            Their services have their own Privacy Policies and comply with GDPR and other data protection regulations.
          </p>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">5. Data Deletion</h2>
          <p className="mb-4">
            You have the right to delete your account and all associated data at any time.
          </p>
          <ul className="list-disc pl-6 mb-4">
            <li className="mb-2">
              <strong>How to delete:</strong> You can find the <strong>"Delete Account"</strong> option directly inside the App settings.
            </li>
            <li className="mb-2">
              <strong>Result:</strong> Upon confirmation, your account, email, expenses, and images will be permanently removed from our servers.
            </li>
          </ul>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">6. Children's Privacy</h2>
          <p className="mb-4">
            Our App is not intended for use by children under the age of 13. We do not knowingly collect personal information from children.
          </p>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">7. Changes to This Policy</h2>
          <p className="mb-4">
            We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.
          </p>
        </section>

        <section className="mb-8">
          <h2 className="text-2xl font-semibold mb-4">8. Contact Us</h2>
          <p className="mb-4">
            If you have any questions about this Privacy Policy, please contact us at: <a href="mailto:smappcorp@gmail.com" className="text-blue-600 hover:underline">smappcorp@gmail.com</a>
          </p>
        </section>
      </div>
    </div>
  );
}
