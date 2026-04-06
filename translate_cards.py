# -*- coding: utf-8 -*-
import os

translations = {
    'ru/mobilnye-prilozheniya.html': [
        ('Aplikacje, które<br>użytkownicy pokochają', 'Приложения, которые<br>полюбят пользователи', 0),
        ('Aplikacje, które', 'Приложения, которые', 0),
        ('użytkownicy pokochają', 'полюбят пользователи', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od nowoczesnego projektowania i budowy bezpiecznego backendu, aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'Мы профессиональные разработчики мобильных приложений. Занимаемся всем процессом: от современного проектирования и создания безопасного бэкенда до тестирования и публикации вашего приложения в App Store и Google Play.', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od projektowania aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'Мы профессиональные разработчики мобильных приложений. Занимаемся всем процессом: от проектирования до тестирования и публикации вашего приложения в App Store и Google Play.', 0),
        ('Co robimy', 'Что мы делаем', 0),
        ('Jedna baza kodu, dwie platformy', 'Одна кодовая база, две платформы', 0),
        ('Jedna aplikacja działa natywnie na obu platformach. Korzystamy z React Native – sprawdzonej technologii używanej przez miliony aplikacji na całym świecie.', 'Одно приложение работает нативно на обеих платформах. Мы используем React Native — проверенную технологию, на которой работают миллионы приложений по всему миру.', 0),
        ('Backend i API', 'Бэкенд и API', 0),
        ('Logika, dane, autoryzacja', 'Логика, данные, авторизация', 0),
        ('Konta użytkowników, bazy danych, płatności – zaprojektujemy i wdrożymy backend dopasowany do wymagań aplikacji.', 'Учетные записи пользователей, базы данных, платежи — мы спроектируем и внедрим бэкенд под требования вашего приложения.', 0),
        ('Piękne i intuicyjne', 'Красивые и интуитивно понятные', 0),
        ('Projektujemy interfejsy z myślą o użytkowniku. Zgodnie z wytycznymi Human Interface Guidelines (Apple) i Material Design (Google).', 'Проектируем интерфейсы с заботой о пользователе. В соответствии с Human Interface Guidelines от Apple и Material Design от Google.', 0),
        ('Publikacja w sklepach', 'Публикация в сторах', 0),
        ('Od konfiguracji do akceptacji', 'От создания аккаунта до модерации', 0),
        ('Zajmiemy się całym procesem publikacji w App Store i Google Play – od konfiguracji konta po przejście przez review. Możemy też zadbać o ASO (optymalizację w sklepie).', 'Мы возьмем на себя весь процесс публикации в App Store и Google Play — от настройки аккаунта до прохождения ревью. Также поможем с ASO (оптимизация страницы в магазине).', 0),
        ('Najczęstsze pytania o aplikacje mobilne', 'Частые вопросы о мобильных приложениях', 0),
        ('Zarządzanie aplikacją (CMS)', 'Управление контентом (CMS)', 0),
        ('Baza danych & API', 'База данных и API', 0),
        ('Integracje zewnętrzne', 'Внешние интеграции', 0),
        ('Najlepsze praktyki iOS/Android', 'Лучшие практики iOS/Android', 0),
        ('Badanie UX', 'UX Исследования', 0),
        ('Prototypowanie UI', 'UI Прототипирование', 0),
        ('Utrzymanie i SLA', 'Поддержка и SLA', 0),
        ('Projektowanie natywne UI/UX', 'Создание нативного UI/UX', 0),
        ('Współdzielona logika biznesowa', 'Общая бизнес-логика', 0),
        ('Zaawansowana analityka', 'Продвинутая аналитика', 0),
        ('Monitorowanie stabilności', 'Мониторинг стабильности', 0)
    ],
    'en/mobile-apps.html': [
        ('Aplikacje, które<br>użytkownicy pokochają', 'Apps that<br>users will love', 0),
        ('Aplikacje, które', 'Apps that', 0),
        ('użytkownicy pokochają', 'users will love', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od nowoczesnego projektowania i budowy bezpiecznego backendu, aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'We are professional mobile app developers. We handle the entire process: from modern design and secure backend development to testing and publishing your app on the App Store and Google Play.', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od projektowania aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'We are professional mobile app developers. We handle the entire process: from design to testing and publishing your app on the App Store and Google Play.', 0),
        ('Co robimy', 'What we do', 0),
        ('Jedna baza kodu, dwie platformy', 'One codebase, two platforms', 0),
        ('Jedna aplikacja działa natywnie na obu platformach. Korzystamy z React Native – sprawdzonej technologii używanej przez miliony aplikacji na całym świecie.', 'One app runs natively on both platforms. We use React Native — a battle-tested technology driving millions of apps worldwide.', 0),
        ('Backend i API', 'Backend & API', 0),
        ('Logika, dane, autoryzacja', 'Logic, data, auth', 0),
        ('Konta użytkowników, bazy danych, płatności – zaprojektujemy i wdrożymy backend dopasowany do wymagań aplikacji.', 'User accounts, databases, payments — we will design and deploy a backend tailored to your app’s needs.', 0),
        ('Piękne i intuicyjne', 'Beautiful and intuitive', 0),
        ('Projektujemy interfejsy z myślą o użytkowniku. Zgodnie z wytycznymi Human Interface Guidelines (Apple) i Material Design (Google).', 'We design user-centric interfaces. True to Apple’s Human Interface Guidelines and Google’s Material Design.', 0),
        ('Publikacja w sklepach', 'Store Publishing', 0),
        ('Od konfiguracji do akceptacji', 'From setup to approval', 0),
        ('Zajmiemy się całym procesem publikacji w App Store i Google Play – od konfiguracji konta po przejście przez review. Możemy też zadbać o ASO (optymalizację w sklepie).', 'We manage the entire publishing process on App Store and Google Play — from account setup to review clearance. We can also handle app store optimization (ASO).', 0),
        ('Najczęstsze pytania o aplikacje mobilne', 'Frequent questions about mobile apps', 0),
        ('Zarządzanie aplikacją (CMS)', 'App Management (CMS)', 0),
        ('Baza danych & API', 'Database & API', 0),
        ('Integracje zewnętrzne', '3rd-Party Integrations', 0),
        ('Najlepsze praktyki iOS/Android', 'iOS/Android Best Practices', 0),
        ('Badanie UX', 'UX Research', 0),
        ('Prototypowanie UI', 'UI Prototyping', 0),
        ('Utrzymanie i SLA', 'Maintenance & SLA', 0),
        ('Projektowanie natywne UI/UX', 'Native UI/UX Design', 0),
        ('Współdzielona logika biznesowa', 'Shared Business Logic', 0),
        ('Zaawansowana analityka', 'Advanced Analytics', 0),
        ('Monitorowanie stabilności', 'Stability Monitoring', 0)
    ],
    'hr/mobilne-aplikacije.html': [
        ('Aplikacje, które<br>użytkownicy pokochają', 'Aplikacije koje će<br>korisnici voljeti', 0),
        ('Aplikacje, które', 'Aplikacije koje će', 0),
        ('użytkownicy pokochają', 'korisnici voljeti', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od nowoczesnego projektowania i budowy bezpiecznego backendu, aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'Mi smo profesionalni kreatori mobilnih aplikacija. Bavimo se cijelim procesom: od modernog dizajna i sigurne izrade backend sustava do testiranja i objave vaše aplikacije na App Storeu i Google Playu.', 0),
        ('Jesteśmy profesjonalnym producentem aplikacji mobilnych. Zajmujemy się całym procesem: od projektowania aż po testy oraz publikację Twojej aplikacji w App Store i Google Play.', 'Mi smo profesionalni kreatori mobilnih aplikacija. Bavimo se cijelim procesom: od dizajna do testiranja i objave vaše aplikacije na App Storeu i Google Playu.', 0),
        ('Co robimy', 'Što radimo', 0),
        ('Jedna baza kodu, dwie platformy', 'Jedna kodna baza, dvije platforme', 0),
        ('Jedna aplikacja działa natywnie na obu platformach. Korzystamy z React Native – sprawdzonej technologii używanej przez miliony aplikacji na całym świecie.', 'Jedna aplikacija radi nativno na obje platforme. Koristimo React Native — dokazanu tehnologiju koja pokreće milijune aplikacija širom svijeta.', 0),
        ('Backend i API', 'Backend i API', 0),
        ('Logika, dane, autoryzacja', 'Logika, podaci, prijava', 0),
        ('Konta użytkowników, bazy danych, płatności – zaprojektujemy i wdrożymy backend dopasowany do wymagań aplikacji.', 'Korisnički računi, baze podataka, plaćanja — dizajnirat ćemo i implementirati backend prilagođen potrebama vaše aplikacije.', 0),
        ('Piękne i intuicyjne', 'Prelijepo i intuitivno', 0),
        ('Projektujemy interfejsy z myślą o użytkowniku. Zgodnie z wytycznymi Human Interface Guidelines (Apple) i Material Design (Google).', 'Dizajniramo sučelja usmjerena na korisnika. U skladu sa smjernicama Human Interface Guidelines (Apple) i Material Design (Google).', 0),
        ('Publikacja w sklepach', 'Objava u trgovinama', 0),
        ('Od konfiguracji do akceptacji', 'Od postavljanja do odobrenja', 0),
        ('Zajmiemy się całym procesem publikacji w App Store i Google Play – od konfiguracji konta po przejście przez review. Możemy też zadbać o ASO (optymalizację w sklepie).', 'Rješavamo cjelokupan proces objavljivanja na App Storeu i Google Playu — od postavljanja računa do odobrenja. Također možemo preuzeti brigu o ASO optimizaciji.', 0),
        ('Najczęstsze pytania o aplikacje mobilne', 'Najčešća pitanja o mobilnim aplikacijama', 0),
        ('Zarządzanie aplikacją (CMS)', 'Upravljanje aplikacijom (CMS)', 0),
        ('Baza danych & API', 'Baza podataka i API', 0),
        ('Integracje zewnętrzne', 'Vanjske integracije', 0),
        ('Najlepsze praktyki iOS/Android', 'Najbolje prakse iOS/Android', 0),
        ('Badanie UX', 'UX Istraživanje', 0),
        ('Prototypowanie UI', 'UI Prototipiranje', 0),
        ('Utrzymanie i SLA', 'Održavanje i SLA', 0),
        ('Projektowanie natywne UI/UX', 'Nativni UI/UX Dizajn', 0),
        ('Współdzielona logika biznesowa', 'Zajednička poslovna logika', 0),
        ('Zaawansowana analityka', 'Napredna analitika', 0),
        ('Monitorowanie stabilności', 'Praćenje stabilnosti', 0)
    ]
}

def run_translation():
    for f_path, replacements in translations.items():
        if os.path.exists(f_path):
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
            for old_text, new_text, mode in replacements:
                content = content.replace(old_text, new_text)
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Translated key strings in {f_path}")
        else:
            print(f"Not found: {f_path}")

run_translation()
