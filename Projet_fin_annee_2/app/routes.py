```index.tsx
import './index.css'
import React from "react";
import { render } from "react-dom";
import { App } from "./App";

render(<App />, document.getElementById("root"));

```
```App.tsx
import React, { useState } from 'react'
import { Navbar } from './components/Navbar'
import { HomePage } from './components/HomePage'
import { AddTripForm } from './components/trips/AddTripForm'
import { SearchTrips } from './components/trips/SearchTrips'
export function App() {
  const [currentPage, setCurrentPage] = useState('home')
  return (
    <div className="flex flex-col min-h-screen bg-gray-50">
      <Navbar setCurrentPage={setCurrentPage} />
      <main className="flex-grow w-full">
        {currentPage === 'home' && <HomePage setCurrentPage={setCurrentPage} />}
        {currentPage === 'add-trip' && <AddTripForm />}
        {currentPage === 'search-trips' && <SearchTrips />}
      </main>
      <footer className="bg-gray-800 text-white py-4 text-center">
        <p className="text-sm">
          © 2023 Covoiturage Pro. Tous droits réservés.
        </p>
      </footer>
    </div>
  )
}

```
```tailwind.config.js
export default {}
```
```index.css
/* PLEASE NOTE: THESE TAILWIND IMPORTS SHOULD NEVER BE DELETED */
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
/* DO NOT DELETE THESE TAILWIND IMPORTS, OTHERWISE THE STYLING WILL NOT RENDER AT ALL */
```
```components/Navbar.tsx
import React, { useState } from 'react'
import { MenuIcon, XIcon, UserIcon, LogInIcon, LogOutIcon } from 'lucide-react'
export const Navbar = ({ setCurrentPage }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const toggleMenu = () => setIsMenuOpen(!isMenuOpen)
  // Simulate login/logout (replace with actual auth logic)
  const toggleLogin = () => setIsLoggedIn(!isLoggedIn)
  return (
    <nav className="bg-blue-600 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <span
              className="text-xl font-bold cursor-pointer"
              onClick={() => setCurrentPage('home')}
            >
              CovoiturePro
            </span>
          </div>
          {/* Desktop menu */}
          <div className="hidden md:flex items-center space-x-4">
            <button
              onClick={() => setCurrentPage('add-trip')}
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Proposer un trajet
            </button>
            <button
              onClick={() => setCurrentPage('search-trips')}
              className="px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              Rechercher un trajet
            </button>
            <button
              onClick={toggleLogin}
              className="flex items-center px-3 py-2 rounded-md hover:bg-blue-700 transition"
            >
              {isLoggedIn ? (
                <>
                  <LogOutIcon className="h-5 w-5 mr-1" />
                  Déconnexion
                </>
              ) : (
                <>
                  <LogInIcon className="h-5 w-5 mr-1" />
                  Connexion
                </>
              )}
            </button>
            {isLoggedIn && (
              <button className="flex items-center px-3 py-2 rounded-md hover:bg-blue-700 transition">
                <UserIcon className="h-5 w-5 mr-1" />
                Mon Profil
              </button>
            )}
          </div>
          {/* Mobile menu button */}
          <div className="flex md:hidden items-center">
            <button
              onClick={toggleMenu}
              className="inline-flex items-center justify-center p-2 rounded-md hover:bg-blue-700 focus:outline-none"
            >
              {isMenuOpen ? (
                <XIcon className="block h-6 w-6" />
              ) : (
                <MenuIcon className="block h-6 w-6" />
              )}
            </button>
          </div>
        </div>
      </div>
      {/* Mobile menu */}
      {isMenuOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-blue-600">
            <button
              onClick={() => {
                setCurrentPage('add-trip')
                setIsMenuOpen(false)
              }}
              className="block px-3 py-2 rounded-md w-full text-left hover:bg-blue-700 transition"
            >
              Proposer un trajet
            </button>
            <button
              onClick={() => {
                setCurrentPage('search-trips')
                setIsMenuOpen(false)
              }}
              className="block px-3 py-2 rounded-md w-full text-left hover:bg-blue-700 transition"
            >
              Rechercher un trajet
            </button>
            <button
              onClick={toggleLogin}
              className="flex items-center px-3 py-2 rounded-md w-full hover:bg-blue-700 transition"
            >
              {isLoggedIn ? (
                <>
                  <LogOutIcon className="h-5 w-5 mr-1" />
                  Déconnexion
                </>
              ) : (
                <>
                  <LogInIcon className="h-5 w-5 mr-1" />
                  Connexion
                </>
              )}
            </button>
            {isLoggedIn && (
              <button className="flex items-center px-3 py-2 rounded-md w-full hover:bg-blue-700 transition">
                <UserIcon className="h-5 w-5 mr-1" />
                Mon Profil
              </button>
            )}
          </div>
        </div>
      )}
    </nav>
  )
}

```
```components/HomePage.tsx
import React from 'react'
import { CarIcon, SearchIcon } from 'lucide-react'
export const HomePage = ({ setCurrentPage }) => {
  return (
    <div className="w-full">
      {/* Hero Section */}
      <section className="bg-blue-600 text-white py-16 px-4">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">
            Covoiturage professionnel simplifié
          </h1>
          <p className="text-xl md:text-2xl mb-8 max-w-3xl mx-auto">
            Économisez sur vos déplacements professionnels et réduisez votre
            empreinte carbone
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <button
              onClick={() => setCurrentPage('add-trip')}
              className="bg-white text-blue-600 hover:bg-gray-100 px-6 py-3 rounded-lg font-semibold text-lg flex items-center justify-center"
            >
              <CarIcon className="mr-2 h-5 w-5" />
              Proposer un trajet
            </button>
            <button
              onClick={() => setCurrentPage('search-trips')}
              className="bg-blue-700 hover:bg-blue-800 text-white px-6 py-3 rounded-lg font-semibold text-lg flex items-center justify-center"
            >
              <SearchIcon className="mr-2 h-5 w-5" />
              Rechercher un trajet
            </button>
          </div>
        </div>
      </section>
      {/* How it works */}
      <section className="py-16 px-4 bg-white">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Comment ça fonctionne
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <div className="bg-blue-100 text-blue-600 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-xl font-bold">1</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">Inscrivez-vous</h3>
              <p className="text-gray-600">
                Créez votre compte en quelques clics et complétez votre profil
                professionnel.
              </p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <div className="bg-blue-100 text-blue-600 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-xl font-bold">2</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">
                Proposez ou recherchez
              </h3>
              <p className="text-gray-600">
                Proposez vos trajets en tant que conducteur ou recherchez des
                trajets disponibles.
              </p>
            </div>
            <div className="bg-gray-50 p-6 rounded-lg text-center">
              <div className="bg-blue-100 text-blue-600 w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-4">
                <span className="text-xl font-bold">3</span>
              </div>
              <h3 className="text-xl font-semibold mb-3">Voyagez ensemble</h3>
              <p className="text-gray-600">
                Confirmez votre réservation et partagez votre trajet avec
                d'autres professionnels.
              </p>
            </div>
          </div>
        </div>
      </section>
      {/* Benefits */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Pourquoi choisir CovoiturePro
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="text-xl font-semibold mb-2">Économique</h3>
              <p className="text-gray-600">
                Réduisez vos frais de déplacement professionnels en partageant
                les coûts.
              </p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="text-xl font-semibold mb-2">Écologique</h3>
              <p className="text-gray-600">
                Contribuez à réduire l'empreinte carbone de votre entreprise.
              </p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="text-xl font-semibold mb-2">Networking</h3>
              <p className="text-gray-600">
                Rencontrez d'autres professionnels et élargissez votre réseau.
              </p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-sm">
              <h3 className="text-xl font-semibold mb-2">Sécurisé</h3>
              <p className="text-gray-600">
                Profils vérifiés et système d'évaluation pour des trajets en
                toute confiance.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

```
```components/trips/AddTripForm.tsx
import React, { useState } from 'react'
import {
  CalendarIcon,
  ClockIcon,
  MapPinIcon,
  UsersIcon,
  CarIcon,
  BanknoteIcon,
} from 'lucide-react'
export const AddTripForm = () => {
  const [formData, setFormData] = useState({
    departureCity: '',
    arrivalCity: '',
    departureDate: '',
    departureTime: '',
    availableSeats: 1,
    carModel: '',
    price: '',
    comment: '',
  })
  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
  }
  const handleSubmit = (e) => {
    e.preventDefault()
    // Here you would send the data to your Flask backend
    console.log('Form submitted:', formData)
    alert('Trajet ajouté avec succès!')
    // Reset form
    setFormData({
      departureCity: '',
      arrivalCity: '',
      departureDate: '',
      departureTime: '',
      availableSeats: 1,
      carModel: '',
      price: '',
      comment: '',
    })
  }
  return (
    <div className="max-w-4xl mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold text-center mb-8">
        Proposer un trajet
      </h1>
      <div className="bg-white rounded-lg shadow-md p-6">
        <form onSubmit={handleSubmit}>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="departureCity"
              >
                <MapPinIcon className="inline-block w-5 h-5 mr-1 text-blue-500" />
                Ville de départ*
              </label>
              <input
                type="text"
                id="departureCity"
                name="departureCity"
                value={formData.departureCity}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Ex: Paris"
              />
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="arrivalCity"
              >
                <MapPinIcon className="inline-block w-5 h-5 mr-1 text-red-500" />
                Ville d'arrivée*
              </label>
              <input
                type="text"
                id="arrivalCity"
                name="arrivalCity"
                value={formData.arrivalCity}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Ex: Lyon"
              />
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="departureDate"
              >
                <CalendarIcon className="inline-block w-5 h-5 mr-1 text-gray-600" />
                Date de départ*
              </label>
              <input
                type="date"
                id="departureDate"
                name="departureDate"
                value={formData.departureDate}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="departureTime"
              >
                <ClockIcon className="inline-block w-5 h-5 mr-1 text-gray-600" />
                Heure de départ*
              </label>
              <input
                type="time"
                id="departureTime"
                name="departureTime"
                value={formData.departureTime}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="availableSeats"
              >
                <UsersIcon className="inline-block w-5 h-5 mr-1 text-gray-600" />
                Nombre de places disponibles*
              </label>
              <select
                id="availableSeats"
                name="availableSeats"
                value={formData.availableSeats}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                {[1, 2, 3, 4, 5, 6, 7].map((num) => (
                  <option key={num} value={num}>
                    {num}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="carModel"
              >
                <CarIcon className="inline-block w-5 h-5 mr-1 text-gray-600" />
                Modèle de voiture*
              </label>
              <input
                type="text"
                id="carModel"
                name="carModel"
                value={formData.carModel}
                onChange={handleChange}
                required
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Ex: Peugeot 308"
              />
            </div>
            <div>
              <label
                className="block text-gray-700 font-medium mb-2"
                htmlFor="price"
              >
                <BanknoteIcon className="inline-block w-5 h-5 mr-1 text-green-600" />
                Prix par passager (€)*
              </label>
              <input
                type="number"
                id="price"
                name="price"
                value={formData.price}
                onChange={handleChange}
                required
                min="0"
                step="0.01"
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="Ex: 15.00"
              />
            </div>
          </div>
          <div className="mt-6">
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="comment"
            >
              Commentaire (facultatif)
            </label>
            <textarea
              id="comment"
              name="comment"
              value={formData.comment}
              onChange={handleChange}
              rows={3}
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Informations complémentaires sur votre trajet..."
            ></textarea>
          </div>
          <div className="mt-8 text-center">
            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg transition"
            >
              Publier ce trajet
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

```
```components/trips/SearchTrips.tsx
import React, { useState } from 'react'
import { SearchIcon, FilterIcon, MapPinIcon, CalendarIcon } from 'lucide-react'
import { TripList } from './TripList'
export const SearchTrips = () => {
  const [searchParams, setSearchParams] = useState({
    departureCity: '',
    arrivalCity: '',
    departureDate: '',
    passengers: 1,
  })
  const [isSearched, setIsSearched] = useState(false)
  // Mock data for demonstration
  const mockTrips = [
    {
      id: 1,
      departureCity: 'Paris',
      arrivalCity: 'Lyon',
      departureDate: '2023-10-15',
      departureTime: '08:30',
      availableSeats: 3,
      price: 25,
      driver: {
        name: 'Thomas D.',
        rating: 4.8,
        trips: 42,
        avatar: 'https://randomuser.me/api/portraits/men/32.jpg',
      },
    },
    {
      id: 2,
      departureCity: 'Paris',
      arrivalCity: 'Lyon',
      departureDate: '2023-10-15',
      departureTime: '10:15',
      availableSeats: 2,
      price: 22,
      driver: {
        name: 'Marie L.',
        rating: 4.9,
        trips: 78,
        avatar: 'https://randomuser.me/api/portraits/women/44.jpg',
      },
    },
    {
      id: 3,
      departureCity: 'Paris',
      arrivalCity: 'Lyon',
      departureDate: '2023-10-15',
      departureTime: '14:00',
      availableSeats: 1,
      price: 28,
      driver: {
        name: 'Jean R.',
        rating: 4.6,
        trips: 23,
        avatar: 'https://randomuser.me/api/portraits/men/67.jpg',
      },
    },
  ]
  const handleChange = (e) => {
    const { name, value } = e.target
    setSearchParams((prev) => ({
      ...prev,
      [name]: value,
    }))
  }
  const handleSubmit = (e) => {
    e.preventDefault()
    // Here you would send the search query to your Flask backend
    console.log('Search submitted:', searchParams)
    setIsSearched(true)
  }
  return (
    <div className="max-w-6xl mx-auto py-8 px-4">
      <h1 className="text-3xl font-bold text-center mb-8">
        Rechercher un trajet
      </h1>
      <div className="bg-white rounded-lg shadow-md p-6 mb-8">
        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-4 gap-4"
        >
          <div>
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="departureCity"
            >
              <MapPinIcon className="inline-block w-5 h-5 mr-1 text-blue-500" />
              Départ
            </label>
            <input
              type="text"
              id="departureCity"
              name="departureCity"
              value={searchParams.departureCity}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Ville de départ"
            />
          </div>
          <div>
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="arrivalCity"
            >
              <MapPinIcon className="inline-block w-5 h-5 mr-1 text-red-500" />
              Arrivée
            </label>
            <input
              type="text"
              id="arrivalCity"
              name="arrivalCity"
              value={searchParams.arrivalCity}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Ville d'arrivée"
            />
          </div>
          <div>
            <label
              className="block text-gray-700 font-medium mb-2"
              htmlFor="departureDate"
            >
              <CalendarIcon className="inline-block w-5 h-5 mr-1 text-gray-600" />
              Date
            </label>
            <input
              type="date"
              id="departureDate"
              name="departureDate"
              value={searchParams.departureDate}
              onChange={handleChange}
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="flex items-end">
            <button
              type="submit"
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-md flex items-center justify-center transition"
            >
              <SearchIcon className="w-5 h-5 mr-2" />
              Rechercher
            </button>
          </div>
        </form>
        {isSearched && (
          <div className="mt-4 pt-4 border-t flex justify-between items-center">
            <p className="text-gray-700">
              <span className="font-medium">Trajets trouvés:</span>{' '}
              {mockTrips.length} résultats de {searchParams.departureCity} à{' '}
              {searchParams.arrivalCity}
            </p>
            <button className="flex items-center text-blue-600 hover:text-blue-800">
              <FilterIcon className="w-4 h-4 mr-1" />
              Filtres
            </button>
          </div>
        )}
      </div>
      {isSearched && <TripList trips={mockTrips} />}
    </div>
  )
}

```
```components/trips/TripList.tsx
import React from 'react'
import { TripCard } from './TripCard'
export const TripList = ({ trips }) => {
  if (!trips || trips.length === 0) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500 text-lg">
          Aucun trajet trouvé pour votre recherche.
        </p>
        <p className="mt-2">Essayez de modifier vos critères de recherche.</p>
      </div>
    )
  }
  return (
    <div className="space-y-4">
      {trips.map((trip) => (
        <TripCard key={trip.id} trip={trip} />
      ))}
    </div>
  )
}

```
```components/trips/TripCard.tsx
import React from 'react'
import {
  MapPinIcon,
  ClockIcon,
  UsersIcon,
  StarIcon,
  CalendarIcon,
} from 'lucide-react'
export const TripCard = ({ trip }) => {
  // Format date for display
  const formatDate = (dateString) => {
    const options = {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
    }
    return new Date(dateString).toLocaleDateString('fr-FR', options)
  }
  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="grid grid-cols-1 md:grid-cols-5 divide-y md:divide-y-0 md:divide-x">
        {/* Time and date */}
        <div className="p-4 flex flex-col justify-center items-center md:items-start">
          <p className="text-2xl font-bold text-blue-600">
            {trip.departureTime}
          </p>
          <p className="text-gray-600 text-sm">
            <CalendarIcon className="inline-block w-4 h-4 mr-1" />
            {formatDate(trip.departureDate)}
          </p>
        </div>
        {/* Route */}
        <div className="p-4 md:col-span-2">
          <div className="flex items-start mb-2">
            <div className="mt-1 mr-3">
              <div className="w-3 h-3 rounded-full bg-blue-500"></div>
              <div className="w-0.5 h-12 bg-gray-300 mx-auto"></div>
              <div className="w-3 h-3 rounded-full bg-red-500"></div>
            </div>
            <div>
              <p className="font-semibold">
                <MapPinIcon className="inline-block w-4 h-4 mr-1 text-blue-500" />
                {trip.departureCity}
              </p>
              <p className="mt-8 font-semibold">
                <MapPinIcon className="inline-block w-4 h-4 mr-1 text-red-500" />
                {trip.arrivalCity}
              </p>
            </div>
          </div>
        </div>
        {/* Driver info */}
        <div className="p-4 flex items-center">
          <img
            src={trip.driver.avatar}
            alt={trip.driver.name}
            className="w-12 h-12 rounded-full mr-3"
          />
          <div>
            <p className="font-medium">{trip.driver.name}</p>
            <div className="flex items-center text-sm">
              <StarIcon className="w-4 h-4 text-yellow-500 mr-1" />
              <span>
                {trip.driver.rating} • {trip.driver.trips} trajets
              </span>
            </div>
          </div>
        </div>
        {/* Price and booking */}
        <div className="p-4 flex flex-col justify-between items-center">
          <div className="text-center mb-3">
            <p className="text-2xl font-bold text-green-600">{trip.price} €</p>
            <p className="text-sm text-gray-600">
              <UsersIcon className="inline-block w-4 h-4 mr-1" />
              {trip.availableSeats} place{trip.availableSeats > 1 ? 's' : ''}{' '}
              disponible{trip.availableSeats > 1 ? 's' : ''}
            </p>
          </div>
          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md transition">
            Réserver
          </button>
        </div>
      </div>
    </div>
  )
} 

```  je veux que tu te considères un expert en design et que tu adaptes le style de ce code à mon projet de covoiturage dont le nom sera ProRide, propose-moi un css adapté qui sera le meme design que ce code, tu as déjà mes fichiers html et .py, donne moi le css qu'il faut, adoptes le meme design que ce code