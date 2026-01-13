import { motion } from 'motion/react';
import { Code2, Bot, Smartphone, Zap, Mail, Phone, Linkedin, MapPin, Clock } from 'lucide-react';

export default function App() {
  const services = [
    {
      icon: Code2,
      title: 'Web Development',
      description: 'Modern, responsive and high-performance web applications using the latest technologies',
    },
    {
      icon: Bot,
      title: 'Chat Bots',
      description: 'Intelligent bots for communication automation and enhanced customer experience',
    },
    {
      icon: Smartphone,
      title: 'Mobile Applications',
      description: 'Cross-platform applications for iOS and Android with native user experience',
    },
    {
      icon: Zap,
      title: 'Automation',
      description: 'Business process optimization through automation of routine tasks and integrations',
    },
  ];

  const contactInfo = [
    {
      icon: Mail,
      label: 'Email',
      value: 'smappcorp@gmail.com',
      href: 'mailto:smappcorp@gmail.com',
    },
    {
      icon: Phone,
      label: 'Phone',
      value: '+48 780-779-546',
      href: 'tel:+48780779546',
    },
    {
      icon: Linkedin,
      label: 'LinkedIn',
      value: 'maxonegeograf',
      href: 'https://linkedin.com/in/maxonegeograf',
    },
  ];

  const technologies = [
    'React Native', 'iOS', 'Android', 'Firebase',
    'Telegram API', 'Docker', 'PostgreSQL', 'Artificial Intelligence', 'Agents'
  ];

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center px-6 border-b border-purple-900/30">
        <div className="max-w-5xl mx-auto text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <h1 className="text-6xl md:text-7xl lg:text-8xl font-bold mb-6 text-white">
              HAMET
            </h1>
            <div className="w-24 h-1 bg-purple-600 mx-auto mb-8"></div>
            <p className="text-xl md:text-2xl text-gray-400 mb-12 max-w-3xl mx-auto">
              Creating digital solutions that work
            </p>
          </motion.div>
        </div>
      </section>

      {/* Services Section */}
      <section className="relative py-24 px-6 border-b border-purple-900/30">
        <div className="max-w-6xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="mb-16 md:pl-10"
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-4 text-white">
              Services
            </h2>
            <div className="w-16 h-1 bg-purple-600"></div>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-px bg-purple-900/30">
            {services.map((service, index) => (
              <motion.div
                key={service.title}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="group bg-gray-950 p-10 hover:bg-gray-900 transition-colors"
              >
                <service.icon className="w-10 h-10 text-purple-500 mb-6" strokeWidth={1.5} />
                
                <h3 className="text-2xl font-bold mb-4 text-white">
                  {service.title}
                </h3>
                
                <p className="text-gray-400 leading-relaxed">
                  {service.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="relative py-24 px-6 border-b border-purple-900/30">
        <div className="max-w-4xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
            className="mb-16"
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-4 text-white">
              Contact
            </h2>
            <div className="w-16 h-1 bg-purple-600"></div>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
            {contactInfo.map((contact, index) => (
              <motion.a
                key={contact.label}
                href={contact.href}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                className="group"
              >
                <contact.icon className="w-8 h-8 text-purple-500 mb-4" strokeWidth={1.5} />
                <p className="text-sm text-gray-500 mb-2 uppercase tracking-wider">{contact.label}</p>
                <p className="text-white group-hover:text-purple-400 transition-colors">
                  {contact.value}
                </p>
              </motion.a>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="relative py-16 px-6">
        <div className="max-w-6xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-12">
            {/* About */}
            <div>
              <h3 className="text-lg font-bold mb-4 text-white">About Developer</h3>
              <p className="text-gray-400 text-sm leading-relaxed">
                Senior mobile and web developer focused on creating quality and scalable solutions. 
                Working with modern technologies and best practices.
              </p>
            </div>

            {/* Technologies */}
            <div>
              <h3 className="text-lg font-bold mb-4 text-white">Technologies</h3>
              <div className="flex flex-wrap gap-2">
                {technologies.map((tech) => (
                  <span 
                    key={tech} 
                    className="text-xs text-gray-400 border border-purple-900/50 px-3 py-1 hover:border-purple-600 hover:text-purple-400 transition-colors"
                  >
                    {tech}
                  </span>
                ))}
              </div>
            </div>

            {/* Info */}
            <div>
              <h3 className="text-lg font-bold mb-4 text-white">Information</h3>
              <div className="space-y-3">
                <div className="flex items-start gap-3">
                  <MapPin className="w-4 h-4 text-purple-500 mt-1 flex-shrink-0" strokeWidth={1.5} />
                  <p className="text-sm text-gray-400">Working remotely worldwide</p>
                </div>
                <div className="flex items-start gap-3">
                  <Clock className="w-4 h-4 text-purple-500 mt-1 flex-shrink-0" strokeWidth={1.5} />
                  <p className="text-sm text-gray-400">Response within 24 hours</p>
                </div>
              </div>
            </div>
          </div>

          {/* Bottom */}
          <div className="pt-8 border-t border-purple-900/30 flex flex-col md:flex-row justify-between items-center gap-4">
            <p className="text-sm text-gray-500">© 2026 All rights reserved</p>
          </div>
        </div>
      </footer>
    </div>
  );
}